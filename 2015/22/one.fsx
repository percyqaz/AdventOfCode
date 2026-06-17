type GameState =
    {
        Mana: int
        PlayerHP: int
        BossHP: int
        Shield: int
        Poison: int
        Recharge: int
        Spent: int
    }

type GameResult =
    | Next of GameState
    | Win of int
    | Lose

let tick(state: GameState): GameResult =
    let new_boss_hp = state.BossHP - (if state.Poison > 0 then 3 else 0)
    if new_boss_hp <= 0 then
        Win state.Spent
    else
        { state with
            BossHP = new_boss_hp
            Shield = max 0 (state.Shield - 1)
            Poison = max 0 (state.Poison - 1)
            Recharge = max 0 (state.Recharge - 1)
            Mana = state.Mana + (if state.Recharge > 0 then 101 else 0)
        } |> Next

let boss_turn(state: GameState): GameResult =
    let dmg = if state.Shield > 0 then 1 else 8
    let new_hp = state.PlayerHP - dmg
    if new_hp <= 0 then
        Lose
    else
        Next { state with PlayerHP = new_hp }

let mm(state: GameState) : GameResult =
    let new_boss_hp = state.BossHP - 4
    if new_boss_hp <= 0 then
        Win (state.Spent + 53)
    else
        { state with
            BossHP = new_boss_hp
            Mana = state.Mana - 53
            Spent = state.Spent + 53
        } |> Next

let drain(state: GameState) : GameResult =
    let new_boss_hp = state.BossHP - 2
    if new_boss_hp <= 0 then
        Win (state.Spent + 73)
    else
        { state with
            PlayerHP = state.PlayerHP + 2
            BossHP = new_boss_hp
            Mana = state.Mana - 73
            Spent = state.Spent + 73
        } |> Next

let shield(state: GameState) : GameResult =
    Next { state with Mana = state.Mana - 113; Shield = 6; Spent = state.Spent + 113 }

let poison(state: GameState) : GameResult =
    Next { state with Mana = state.Mana - 173; Poison = 6; Spent = state.Spent + 173 }

let recharge(state: GameState) : GameResult =
    Next { state with Mana = state.Mana - 229; Recharge = 5; Spent = state.Spent + 229 }

let compose(f: GameState -> GameResult) =
    function
    | Next s -> f s
    | Win spent -> Win spent
    | Lose -> Lose

let init = {
    PlayerHP = 50
    BossHP = 55
    Shield = 0
    Poison = 0
    Recharge = 0
    Mana = 500
    Spent = 0
}

let mutable states = [init]
let turn(state: GameState) : GameResult list =
    let ticked = tick state
    seq {
        if state.Mana >= 53 then yield compose mm ticked
        if state.Mana >= 73 then yield compose drain ticked
        if state.Mana >= 113 then yield compose shield ticked
        if state.Mana >= 173 then yield compose poison ticked
        if state.Mana >= 229 then yield compose recharge ticked
    }
    |> List.ofSeq
    |> List.map (compose tick)
    |> List.map (compose boss_turn)

let mutable m = 98990829
for i = 0 to 10 do
    states <-
        List.collect turn states
        |> List.choose (function Win spent -> m <- min m spent; None | Lose -> None | Next s -> Some s)
printfn "%i" m

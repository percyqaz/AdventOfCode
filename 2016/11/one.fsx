open System

type Item =
    | Generator of char
    | Chip of char

type Floor =
    {
        Generators: Set<char>
        Chips: Set<char>
    }

    static member Empty = { Generators = Set.empty; Chips = Set.empty }
    
    member this.Remove(item: Item) : Floor =
        match item with
        | Generator g -> { this with Generators = this.Generators.Remove(g) }
        | Chip c -> { this with Chips = this.Chips.Remove(c) }
    
    member this.Add(item: Item) : Floor =
        match item with
        | Generator g -> { this with Generators = this.Generators.Add(g) }
        | Chip c -> { this with Chips = this.Chips.Add(c) }

    member this.IsSafe : bool =

        let is_chip_fried(chip: char) : bool =
            let has_power = this.Generators.Contains chip
            let generator_exists = not(Set.isEmpty this.Generators)
            generator_exists && not has_power

        this.Chips |> Set.exists is_chip_fried |> not
    static member Create ([<ParamArray>] items: Item array) =
        Array.fold (fun (floor: Floor) (item: Item) -> floor.Add item) Floor.Empty items

    member this.ToArray() : Item array =
        let chips = Seq.map Chip this.Chips
        let generators = Seq.map Generator this.Generators

        Array.ofSeq (Seq.append chips generators)

    override this.ToString() : string =
        "/" + String(Set.toArray this.Chips) + "|" + String(Set.toArray this.Generators) + "/"

type Direction =
    | Up
    | Down

    member this.Offset =
        match this with
        | Up -> 1
        | Down -> -1

type Move =
    | One of Direction * Item
    | Two of Direction * Item * Item

    member this.Direction =
        match this with
        | One (direction, _) -> direction
        | Two (direction, _, _) -> direction

type State =
    {
        Level: int
        Floors: Floor array
    }

    static member Create ([<ParamArray>] floors: Floor array) : State =
        { Level = 0; Floors = floors }

    member this.CurrentFloor = this.Floors.[this.Level]

    member this.Move(move: Move) : State =
        let current_level = this.Level
        let current_floor = this.Floors.[current_level]
        let target_level = this.Level + move.Direction.Offset
        let target_floor = this.Floors.[target_level]

        let apply_to_floor (app: Floor -> Item -> Floor, move: Move, floor: Floor) : Floor =
            match move with
            | One (_, item) -> app floor item
            | Two (_, item1, item2) -> app (app floor item1) item2

        let add_to_floor(move: Move, floor: Floor) = apply_to_floor(_.Add, move, floor)
        let remove_from_floor(move: Move, floor: Floor) = apply_to_floor(_.Remove, move, floor)

        let new_floors = Array.copy this.Floors
        new_floors.[current_level] <- remove_from_floor(move, current_floor)
        new_floors.[target_level] <- add_to_floor(move, target_floor)

        { Level = target_level; Floors = new_floors }

    member this.NextStates() : State seq =

        let possible_items = this.CurrentFloor.ToArray()
        let up_possible = this.Level + 1 < this.Floors.Length
        let down_possible = this.Level > 0

        let up_suggestions =
            seq {
                for i = 0 to possible_items.Length - 1 do
                    for j = i + 1 to possible_items.Length - 1 do
                        yield Two(Up, possible_items.[i], possible_items.[j])
            }

        let down_suggestions =
            seq {
                for item in possible_items do
                    yield One(Down, item)
            }

        let priority_moves = 
            seq {
                if up_possible then yield! up_suggestions
                if down_possible then yield! down_suggestions
            }

        let backup_moves =
            seq {
                for item in possible_items do
                    yield One(Up, item)
            }

        let mutable something_yielded = false
        let try_moves(moves: Move seq) : State seq =
            seq {
                for move in moves do
                    let next_state = this.Move(move)
                    if next_state.IsSafeAfterMove then
                        something_yielded <- true
                        yield next_state
            }

        seq {
            yield! try_moves priority_moves
            if not something_yielded && up_possible then
                yield! try_moves backup_moves
        }

    member this.IsSafeAfterMove = this.CurrentFloor.IsSafe

    override this.ToString() : string =
        let format_floor(level: int, floor: Floor) =
            let is_current = this.Level = level
            let format = if is_current then sprintf "*%O" else sprintf " %O"
            format floor

        this.Floors
        |> Array.mapi (fun level floor -> format_floor(level, floor))
        |> String.concat "\n"

    member this.Solution : State =
        let all_objects = this.Floors |> Array.collect (fun x -> x.ToArray())

        let init_floor(index: int) =
            let is_last = index + 1 = this.Floors.Length
            if is_last then Floor.Create(all_objects) else Floor.Empty

        let floors = Array.init this.Floors.Length init_floor

        { Floors = floors; Level = this.Floors.Length - 1 }

let initial_state =
    State.Create(
        Floor.Create(Generator 'T', Chip 'T', Generator 'P', Generator 'S'),
        Floor.Create(Chip 'P', Chip 'S'),
        Floor.Create(Generator 'M', Chip 'M', Generator 'R', Chip 'R'),
        Floor.Create()
    )

let mutable current_states = [|initial_state|]
let mutable seen_states = Set.singleton(initial_state.ToString())
let mutable moves = 0
let next_states() : State seq =

    let not_already_seen(new_state: State) =
        let state_string = new_state.ToString()
        let already_seen = seen_states.Contains(state_string)
        seen_states <- seen_states.Add(state_string)
        not already_seen

    let possible_next_states(state: State) : State seq =
        seq {
            for new_state in state.NextStates() do
                if not_already_seen(new_state) then
                    yield new_state
        }

    seq {
        for state in current_states do
            yield! possible_next_states(state)
    }

let desired_state = initial_state.Solution.ToString()

let desired_state_reached() =
    seen_states.Contains(desired_state)

while not(desired_state_reached()) do
    current_states <- next_states() |> Array.ofSeq
    moves <- moves + 1

printfn "desired state after %i moves" moves
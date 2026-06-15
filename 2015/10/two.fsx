[<Struct>]
type Piece =
    {
        Digit: int
        Count: int
    }
    member this.Next : Piece list =
        Piece.FromString(this.Count.ToString()) @ [{ Count = 1; Digit = this.Digit }]

    static member FromString (s: string) : Piece list =
        let mutable n = 0
        let mutable c = ' '
        let mutable output = []
        for i = s.Length - 1 downto 0 do
            let digit = s.[i]
            if digit = c then
                n <- n + 1
            else
                if n > 0 then
                    output <- { Digit = int c - int '0'; Count = n } :: output
                c <- digit
                n <- 1
        if n > 0 then
            output <- { Digit = int c - int '0'; Count = n } :: output
        output

    [<TailCall>]
    static member Pack (pieces: Piece list) : Piece list =
        
        let rec loop acc pieces =
            match pieces with
            | [] -> List.rev acc
            | [x] -> List.rev (x :: acc)
            | x :: y :: xs ->
                if x.Digit = y.Digit then
                    loop acc ({ Digit = x.Digit; Count = x.Count + y.Count } :: xs)
                else
                    loop (x :: acc) (y :: xs)
        loop [] pieces

    static member NextPieces (pieces: Piece list) : Piece list =
        pieces |> List.collect _.Next |> Piece.Pack

    static member Length (pieces: Piece list) : int =
        pieces |> List.sumBy (fun p -> p.Count)

let mutable pieces = Piece.FromString("1113222113")
for i = 1 to 50 do
    pieces <- Piece.NextPieces pieces
printfn "%i" (Piece.Length(pieces))
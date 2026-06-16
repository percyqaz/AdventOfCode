let MAX = 2_000_000
let data : int array = Array.zeroCreate MAX

for i in 1 .. MAX - 1 do
    for j in 0 .. i .. min(i * 50) (MAX - 1) do
        data[j] <- data[j] + i * 11
data.[0] <- 0
Array.findIndex (fun x -> x >= 36000000) data |> printfn "%d"

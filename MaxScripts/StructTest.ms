struct KPoint
(
    x,
    y,
    z,
    function Init x_ y_ z_ =
    (
        x = x_
        y = y_
        z = z_
    ),
    function Print =
    (
        format "x = %, y = %, z = %\n" x y z
    )
)
a = KPoint()
a.Init 1 3 5
a.Print()
b = [1,3,5]
c = [2,2,2]
d = b + c

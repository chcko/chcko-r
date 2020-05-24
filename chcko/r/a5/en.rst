.. raw:: html

    %path = "maths/differential/introduction"
    %kind = chindnum["texts"]
    %level = 12
    <!-- html -->

We will use the concepts:

- variable/value
- change
- velocity

Variable/Value
==============

English is a historical mix of two languages.
So there are two words of many things.
*Change*, for example, can also be called *vary*.

Something that can change is a *variable*.

*Choose* or *select*: Again two words with same meaning.
I use *select* here.

We can use numbers to select something.
Numbers can be used to select *anything*, just like words.
Just that, numbers are created by counting, which is easier than words.
You know, words come from strange origins,
with more words meaning the same thing, and so on.

How to select with a number?
Easy:

- the third apple or apple number 3
- prisoner: number 9
- position: 120 meters away from the start

A selection is also called *value*.
I know, yet another word: choose, select, value.
*Value* is used together with the word *variable*.

Variable = {value1, value2, ...}
Position = {10m , 20m, ..., 120m, ...}

A variable assumes one *value* at a time, *exclusively*.
So the car could be at position

- 20m at one time and
- 120m at another time
- but not be in two positions at the same time

The position changes: That is why we call it a variable.
What changes is the *value* of the variable.

Note that in english *a* introduces a *variable*,
while *the* introduces a *value* of a variable.

Change
======

Changes often are gradual.
The opposite of a gradual change would be a random change.

The change is expressed with subtraction: `-`.

For example:
Your *height* changes,
i.e. there is a distance between the ticks at the door frame.

Let's abbreviate height by `y`.

Because previous generations still learned old greek,
they abbreviated distance with a greek D: Δ.

`Δh_1 = h_1 - h_0`.

`Δ` alone is not a number.
It means the distance between two numbers.

Note, that distances like `Δh` are new *extensive* variables,
which means, that they count the possible ticks in between `h_0` and `h_1`.
They can also be added, meaning that it makes sense to add them:

`y = Σ Δy_i = Δy_1 + Δy_2 + ...`.

Of course you could also add `y_0` and `y_1`,
but what sense would it make?

.. show one person above other

Also note, that `y_0` and `y_1` can be seen as distance to `0`
instead of the name of the value ( = point = tick).
I prefer to see it as the name of the value.
The distance to `0` is a very convenient naming scheme, though.

If the distance is vary small one uses ``d`` instead of ``Δ``.

`dy = y + dy - y`.

`d` is called *differential*, while `Δ` is called *delta*,
because that is what the `D` is called in greek.

If `d` is used,
then the sum `Σ` becomes `∫`,
and is called integral.

Velocity
========

How fast a value changes is again a variable.
It is called *speed* or *velocity* 

Instead of just saying

- the car position changes or
- my height changes

it is important to be able to tell how fast,
to tell the velocity.

To describe velocity of change of the value of one variable
we need *another variable*.
Often this other variable is *time*, but it could be something else.
If there is no other variable specified, then it is implicitly *time*,
or better our time feeling, given by how fast our brain thinks.

With our height example,
we have two variables:

1) Height `y`: The distance from the floor to the top of your head.

2) Age `x`: The number of years that have passed since your birth.

.. show door frame, ticks on one side, years on the other
   draw a line linking year with height
   turn one axis (drawn variable) to form a coordinate system

To tell the velocity

- of the change of (the value of) your height

compared

- to the change of (the value of) your age

we *divide* the changes, i.e. the differences:

`v = Δy/Δx`

Now you wonder:
Why *divide*?
*Because* then you can *multiply* to get back the difference:

`Δy = v Δx`

And you can sum to get back the height:

`y = Σ Δy = Σ v Δx`

With small distances (*differentials*) this is written:

`v = dy/dx`

And having `v`, the velocity of `y`,
we can get back `y` by multiplying and summing:

`y = ∫ dy = ∫ v dx`.

Instead of

- velocity of change of height `y` with respect to age `x`

one normally says

- *derivative* of height `y` with respect to age `x`



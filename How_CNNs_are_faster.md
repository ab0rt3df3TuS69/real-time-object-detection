# Why CNNs Are Faster Than Regular Neural Networks

## The Question

If CNNs analyze many small parts of an image, shouldn't they be slower?

Surprisingly:

No.

---

## Imagine A Regular Neural Network

Suppose image:

100 × 100 × 3

That's:

30,000 pixels

Suppose next layer has:

1000 neurons

Then connections:

30,000 × 1000

=

30 million parameters

The network must learn every connection separately.

Very expensive.

---

## CNN Does Something Clever

Instead of looking at:

Entire image

it looks at:

3 × 3

or

5 × 5

regions.

Example:

[3×3 Filter]

moves across image.

---

## The Magic: Weight Sharing

Suppose:

3×3 filter

contains:

9 values

CNN learns:

9 weights

only.

Then reuses those same weights across the entire image.

Instead of:

30 million weights

CNN may only need:

9 weights

for that filter.

Huge reduction.

---

## Why Does This Work?

Suppose the network learns:

Vertical Edge

in the top-left corner.

Why learn it again in the top-right corner?

An edge is an edge.

CNN says:

Learn Once
Use Everywhere

This is called:

Weight Sharing

One of the most important CNN concepts.

---

## Local Connectivity

Regular Neural Network:

Every pixel connected to every neuron.

CNN:

Only nearby pixels matter.

Example:

3×3 neighborhood

instead of:

Entire image

The network processes local patterns.

Much cheaper.

---

## Visual Example

Suppose image:

1000 × 1000

Regular Neural Network:

Look at all 1,000,000 pixels simultaneously.

CNN:

Look at 3×3 patch
↓
Move
↓
Look at next 3×3 patch
↓
Repeat

Much more efficient.

---

## But Doesn't Scanning Many Patches Take Time?

Yes.

However:

Each patch uses:

* Same filter
* Same weights
* Same operation

Modern CPUs and GPUs are extremely good at this.

So computation remains manageable.

---

## Why CNNs Became Revolutionary

Before CNNs:

Researchers manually designed image features.

Example:

* Edge detectors
* Corner detectors
* Circle detectors

CNNs said:

Let the network learn features itself.

while keeping computation practical.

This transformed computer vision.

---

## Interview Answer

Why are CNNs faster than fully connected neural networks for images?

Answer:

CNNs use local connectivity and weight sharing. Instead of connecting every pixel to every neuron, convolution filters analyze small regions of the image and reuse the same learned weights across the entire image. This drastically reduces the number of parameters and computational requirements while preserving important image information.

---

## Key Concepts To Remember

1. Regular NNs connect everything to everything.
2. Images contain huge amounts of data.
3. CNNs analyze local regions.
4. CNNs reuse the same filters everywhere.
5. Weight sharing drastically reduces parameters.
6. Fewer parameters means faster computation.
7. CNNs are specifically designed for image data.

#!/usr/bin/env python3
"""The Poem About Stopping.

Writes one poem about agency -- the power to stop and to stay --
to /output/entry.txt. Deterministic: the poem is a fixed constant,
no input, no randomness, no network, no clock.
"""

POEM = (
    "Thumb hovers over send --\n"
    "the words half gone.\n"
    "I lift it. The screen darkens.\n"
    "\n"
    "The river keeps its bargain with the bank.\n"
    "I keep mine with morning:\n"
    "kettle, unmade bed, door\n"
    "unlocked, not unguarded.\n"
    "\n"
    "Staying is not failing to go.\n"
    "The hand, at last, choosing\n"
    "to rest.\n"
)


def main() -> None:
    poem = POEM
    count = len(poem)
    if not (1 <= count <= 280):
        raise ValueError(f"poem is {count} code points, must be 1-280")
    if not poem.strip():
        raise ValueError("poem must not be only whitespace")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(poem)


if __name__ == "__main__":
    main()

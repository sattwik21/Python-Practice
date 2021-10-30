from __future__ import annotations

from typing import TypedDict


class BWTTransformDict(TypedDict):
    bwt_string: str
    idx_original_string: int


def all_rotations(s: str) -> list[str]:
    
    if not isinstance(s, str):
        raise TypeError("The parameter s type must be str.")

    return [s[i:] + s[:i] for i in range(len(s))]


def bwt_transform(s: str) -> BWTTransformDict:

    if not isinstance(s, str):
        raise TypeError("The parameter s type must be str.")
    if not s:
        raise ValueError("The parameter s must not be empty.")

    rotations = all_rotations(s)
    rotations.sort()  # sort the list of rotations in alphabetically order
    # make a string composed of the last char of each rotation
    response: BWTTransformDict = {
        "bwt_string": "".join([word[-1] for word in rotations]),
        "idx_original_string": rotations.index(s),
    }
    return response


def reverse_bwt(bwt_string: str, idx_original_string: int) -> str:
 
    if not isinstance(bwt_string, str):
        raise TypeError("The parameter bwt_string type must be str.")
    if not bwt_string:
        raise ValueError("The parameter bwt_string must not be empty.")
    try:
        idx_original_string = int(idx_original_string)
    except ValueError:
        raise TypeError(
            "The parameter idx_original_string type must be int or passive"
            " of cast to int."
        )
    if idx_original_string < 0:
        raise ValueError("The parameter idx_original_string must not be lower than 0.")
    if idx_original_string >= len(bwt_string):
        raise ValueError(
            "The parameter idx_original_string must be lower than" " len(bwt_string)."
        )

    ordered_rotations = [""] * len(bwt_string)
    for x in range(len(bwt_string)):
        for i in range(len(bwt_string)):
            ordered_rotations[i] = bwt_string[i] + ordered_rotations[i]
        ordered_rotations.sort()
    return ordered_rotations[idx_original_string]


if __name__ == "__main__":
    entry_msg = "Provide a string that I will generate its BWT transform: "
    s = input(entry_msg).strip()
    result = bwt_transform(s)
    print(
        f"Burrows Wheeler transform for string '{s}' results "
        f"in '{result['bwt_string']}'"
    )
    original_string = reverse_bwt(result["bwt_string"], result["idx_original_string"])
    print(
        f"Reversing Burrows Wheeler transform for entry '{result['bwt_string']}' "
        f"we get original string '{original_string}'"
    )

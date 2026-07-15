# Scrabble Game Engine - Foundations of Programming (FP)

A Python programming project developed for the FP course (2025/2026) at Instituto Superior Técnico (IST), focusing on functional programming.

### Evaluation
* Final Grade: 18.6
	* Automated Assessment: 15.6/16.0
	* Code Quality: 3.0/4.0

### Project Features
* Board and Tile Validation: Implementation of a standard 15x15 board state with boundary detection, pattern matching, and letter verification
* Pseudo-Random Distribution: Custom Fisher-Yates shuffle algorithm using XORShift operations to shuffle tile sets
* Word Checks: Validates if words fit the board, connect with existing letters, and match player tiles.
* Game Loop: Coordinates multiple players, scores, tile swapping, and turn choices.

### Run

Load the script using Python:
```bash
python3 FP2526P1.py
```
Launch game with 2 players, custom tile scores, and seed
```python
scrabble(2, saco, pontos, 12345)
```

# (no name)
CF 401 Data Structures Whiteboard Challenge

Mock Interviews

## Challenge
Ask the Candidate the following question:

You are working with a file structure with only at most 2 files or folder. Each file directory has either one or two folders/files.

Comparing two file different file directories, create a method that takes in 2 directory structures and compares both and determines weather or not they have the same number of individual files.

The following will come back as true:

```
Each directoy structure has 5 individual files

			 O
			/ \
		  Fol fol
		  /     \
		fol     fol
		/\		 /\
	   X  fol     X  X
		   /\
		   X X

	   	     O
			/ \
		  Fol fol
		  /     \
		fol     fol
		/\		 /\
	   X  X     X  fol
					/\
				   X  X
```

The following will come back as false:

```
One tree has 4 files, while the other has 5

			 O
			/ \
		  Fol fol
		  /     \
		fol     fol
		/\		 /\
	   X  X     X  X



	   	     O
			/ \
		  Fol fol
		  /     \
		fol     fol
		/\		 /\
	   X  X     X  fol
					/\
				   X  X
```

## Whiteboard
![whiteboard](../../assets/compare-trees.jpg)

### Original Instructions
https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-19/interview-02.html

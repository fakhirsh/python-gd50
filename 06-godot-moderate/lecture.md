# Godot 4

# Today's Lecture Contents

## Lecture Source Code
- [Github Repo: Godot 4 Platformer 01](https://github.com/fakhirsh/python-gd50/tree/main/05-godot-basics)

## Project 1: More on Input
1. Creating a new project
1. Adding a new node (generic Node)
    1. Save the scene as `myscene.tscn`
    1. Add 2 child nodes (`Sprite2D` and a `Button` node)
        1. Assign a texture to sprite 2d node called the `Player`
        1. Set the text of the first button to `Click Me`
            1. Attach a C# script to the `Button` node
            1. Add the following code:
                ```C#
                public override void _Ready()
                {
                    this.Pressed += OnButtonPressed;
                    this.ButtonUp += OnButtonUp;
                    this.ButtonDown += OnButtonDown;
                    this.MouseEntered += OnMouseEntered;
                }
                .....
                ```
    1. Add C# script to the sprite node
        ```C#
        public override void _Ready()
        {
            GD.Print("Sprite _Ready (load)");
        }
        public override void _Process(double delta)
        {
            GD.Print("Sprite _Process (update)");
        }
        ```
    


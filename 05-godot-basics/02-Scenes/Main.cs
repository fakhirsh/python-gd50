using Godot;
using System;

public partial class Main : Node2D
{
	PackedScene packedScene;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		packedScene = GD.Load<PackedScene>("res://Enemy.tscn");
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}

    public override void _UnhandledInput(InputEvent @event)
    {
        if (@event is InputEventMouseButton mouseEvent){
			// create instance of Sprite scene
			// SHOULD BE THE ROOT NODE OF THE SCENE
			Enemy enemy = packedScene.Instantiate<Enemy>();
			// Set the position of the instance
            enemy.Position = GetGlobalMousePosition();
            // Add the instance to the scene
            AddChild(enemy);
		}
    }
}

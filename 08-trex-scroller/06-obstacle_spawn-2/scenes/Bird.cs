using Godot;
using System;

public partial class Bird : Area2D
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		this.Position += new Vector2(-GetParent<Main>().speed*1.3f, 0);
	}
}

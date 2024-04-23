using Godot;
using System;

public partial class Root : Node2D
{
	// Called when the node enters the scene tree for the first time.
	private AudioStreamPlayer music;
	public override void _Ready()
	{
		music = GetNode<AudioStreamPlayer>("Music");
		music.Play();
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}
}

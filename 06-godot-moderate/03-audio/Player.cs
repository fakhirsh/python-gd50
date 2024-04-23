using Godot;
using System;

public partial class Player : Sprite2D
{
	[Export]
	public int SPEED{set;get;} = 500;
	// Called when the node enters the scene tree for the first time.
	private AudioStreamPlayer music;
	public override void _Ready()
	{
		// GD.Print("Player is ready");
		// var sound1 = GetNode<AudioStreamPlayer2D>("Sound1");
		// sound1.Stream = GD.Load<AudioStream>("res://music.mp3");
		// sound1.Play();
		// GD.Print(sound1);

		

	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		// handle arrow key presses
		if(Input.IsActionPressed("ui_up")){
			Position += new Vector2(0, -1) * (float)(SPEED * delta);
		}
		if(Input.IsActionPressed("ui_down")){
			Position += new Vector2(0, 1) * (float)(SPEED * delta);
		}
		if(Input.IsActionPressed("ui_left")){
			Position += new Vector2(-1, 0) * (float)(SPEED * delta);
		}
		if(Input.IsActionPressed("ui_right")){
			Position += new Vector2(1, 0) * (float)(SPEED * delta);
		}
	}

}

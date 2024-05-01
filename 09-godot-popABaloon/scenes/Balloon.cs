using Godot;
using System;

public partial class Balloon : Node2D
{
	public bool popped = false;
	public bool remove = false;
	// speed
	[Export]
	public float Speed = 100.0f;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		var area = GetNode<Area2D>("Area2D");
		area.Connect("area_entered", new Callable(this, nameof(OnCollision)));
		area.Connect("body_entered", new Callable(this, nameof(OnCollision)));
	}

	private void OnCollision(Node body)
	{
		var parent = body.GetParent();
		if (parent is Player)
		{
			if (!popped)
			{
				var sprite = GetNode<AnimatedSprite2D>("AnimatedSprite2D");
				sprite.Play("pop");
				sprite.Connect("animation_finished", new Callable(this, nameof(OnAnimationFinished)));
				popped = true;

				////////////////////////////
				// Add 1 point to the score:
				//
				// 
				////////////////////////////

				var popSound = GetNode<AudioStreamPlayer2D>("PopSound");
				popSound.Play();
			}
		}
	}

	private void OnAnimationFinished()
	{
		remove = true;
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		Position += new Vector2(0, (float)(-Speed * delta));
		if (popped)
		{
			
		}		
	}
}

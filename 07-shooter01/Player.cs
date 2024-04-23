using Godot;
using System;

public partial class Player : Node2D
{
	[Export]
	public int Speed = 230; // How fast the player will move (pixels/sec).

	PackedScene bulletScene;
	public int Lives = 3;

	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		bulletScene = GD.Load<PackedScene>("res://bullet.tscn");
		// var area = GetNode<Area2D>("PlayerArea2D");
		// area.Connect("area_entered", new Callable(this, nameof(OnCollision)));
		// area.Connect("body_entered", new Callable(this, nameof(OnCollision)));
	}

	// private void OnCollision(Node body)
	// {
	// 	GD.Print("Collision with " + body.Name);
	// 	if(body.Name == "EnemyArea2D"){	
	// 		lives--;
	// 		if (lives <= 0)
	// 		{
	// 			QueueFree();
	// 		}
	// 	}
	// }

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		if(Input.IsActionPressed("player_right"))
		{
			Position += this.Transform.Y.Normalized() * (float)(Speed * delta);
		}
		if(Input.IsActionPressed("player_left"))
		{
			Position += this.Transform.Y.Normalized() * (float)(-1 * Speed * delta);
		}
		if(Input.IsActionPressed("player_down"))
		{
			Position += this.Transform.X.Normalized() * (float)(-1 * Speed * delta);
		}
		if(Input.IsActionPressed("player_up"))
		{
			Position += this.Transform.X.Normalized() * (float)(Speed * delta);
		}
		Rotation = (GetGlobalMousePosition() - GlobalPosition).Angle();
	}

	// _Input is called when the left mouse button is pressed.
	public override void _UnhandledInput(InputEvent @event)
	{
		if(Input.IsActionJustPressed("fire_pressed"))
		{
			var bullet = bulletScene.Instantiate<Bullet>();
			bullet.Position = Position;
			bullet.Rotation = Rotation;
			GetParent().AddChild(bullet);
		}
	}
	
}

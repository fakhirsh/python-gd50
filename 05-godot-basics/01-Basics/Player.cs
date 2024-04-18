using Godot;
using System;

public partial class Player : Sprite2D
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		GD.Print("Player _Ready (load)");
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		Sprite2D child = GetNode<Sprite2D>("child");
		child.RotationDegrees += 1;
		
		float AMOUNT = (float)(500.0 * delta);
		if (Input.IsActionPressed("ui_up"))
		{
			this.Position += new Vector2(0, -AMOUNT);
		}
		if (Input.IsActionPressed("ui_down"))
		{
			this.Position += new Vector2(0, AMOUNT);
		}
		if (Input.IsActionPressed("ui_left"))
		{
			this.Position += new Vector2(-AMOUNT, 0);
		}
		if (Input.IsActionPressed("ui_right"))
		{
			this.Position += new Vector2(AMOUNT, 0);
		}
	}

	public override void _Input(InputEvent @event)
	{
		if (@event is InputEventKey keyEvent && keyEvent.Pressed)
		{
			if (keyEvent.Keycode == Key.T)
			{
				GD.Print("T was pressed");
			}
		}
	}

}

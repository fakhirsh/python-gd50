using Godot;
using System;

public partial class Button1 : Button
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		this.Pressed += OnButtonPressed;
		this.ButtonUp += OnButtonUp;
		this.ButtonDown += OnButtonDown;
		this.MouseEntered += OnMouseEntered;
	}

	private void OnButtonPressed()
	{
		GD.Print("Button 1 pressed!");
	}

	private void OnButtonUp()
	{
		GD.Print("Button 1 up!");
	}

	private void OnButtonDown()
	{
		GD.Print("Button 1 down!");
	}

	private void OnMouseEntered()
	{
		GD.Print("Mouse entered button 1!");
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}
}

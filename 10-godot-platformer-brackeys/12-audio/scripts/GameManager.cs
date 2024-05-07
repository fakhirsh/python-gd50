using Godot;
using System;

public partial class GameManager : Node
{
	public int Score = 0;

	public void AddScore(int score)
	{
		Score += score;
		GD.Print("Score: " + Score);

		var scorelbl = GetParent().GetNode<Node>("Labels").GetNode<Label>("score");
		scorelbl.Text = "You collected " +  Score + " coins";
	}
}

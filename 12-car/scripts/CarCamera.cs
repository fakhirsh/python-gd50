using Godot;
using System;

public partial class CarCamera : Camera3D
{
    float lerpSpeed = 3.0f;
    float cameraDistance = 6.0f;
    float fixedYDistance = 4.0f; // Adjust this to set the fixed Y distance above the car
    Node3D target;

    public override void _Ready()
    {
        target = GetParent<Node3D>();
    }

    public override void _Process(double delta)
    {
        if (target == null)
        {
            return;
        }

        var targetPosition = target.GlobalTransform.Origin;
        var cameraPosition = GlobalTransform.Origin;

        // Calculate direction while locking the Y axis
        var direction = (new Godot.Vector3(cameraPosition.X, 0, cameraPosition.Z) - new Godot.Vector3(targetPosition.X, 0, targetPosition.Z)).Normalized();

        // Calculate the desired position
        var desiredPosition = targetPosition + direction * cameraDistance;
        desiredPosition.Y = targetPosition.Y + fixedYDistance;

         // Interpolate the position smoothly
        var interpolatedPosition = new Godot.Vector3(
            Mathf.Lerp(cameraPosition.X, desiredPosition.X, (float)(lerpSpeed * delta)),
            desiredPosition.Y, // Keep Y position fixed
            Mathf.Lerp(cameraPosition.Z, desiredPosition.Z, (float)(lerpSpeed * delta))
        );

        // Update the camera's transform
        GlobalTransform = new Transform3D(GlobalTransform.Basis, interpolatedPosition);
        LookAt(new Godot.Vector3(targetPosition.X, targetPosition.Y + fixedYDistance, targetPosition.Z), new Godot.Vector3(0, 1, 0));
    }
}

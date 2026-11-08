{ pkgs, ... }:
{
  name = "hapyscript";

  # Stacks come from devenv.stacks.nix, pulled in by devenv.yaml. Put
  # project-specific tools here; machine-only settings go in devenv.local.nix.
  packages = with pkgs; [ ];

  # env.DATABASE_URL = "...";
  # services.postgres.enable = true;
}

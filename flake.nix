{
  description = "AOC 2024";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            (python312.withPackages (ps: with ps; [
              python-lsp-server
              python-lsp-black
              pylsp-mypy
              pylsp-rope
              python-lsp-ruff
              ujson
              isort

              more-itertools
              networkx
            ]))
          ];
        };
      });
}

{
  description = "Web-based GLTF/GLB viewer with Flask";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        python = pkgs.python312.withPackages (ps: with ps; [
          flask
        ]);
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [ python ];

          shellHook = ''
            echo "GLTF Viewer - Development Environment"
            echo "Python: $(python --version)"
            echo ""
            echo "Run: python app.py"
            echo "Then open: http://localhost:5000"
          '';
        };

        packages.default = pkgs.writeShellScriptBin "gltf-viewer" ''
          cd ${self}
          ${python}/bin/python app.py
        '';
      }
    );
}

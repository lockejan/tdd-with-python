{
  description = "A basic flake with a dev shell for a python37 django toy project";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system};
      in {
        devShell = pkgs.mkShell {
          nativeBuildInputs = with pkgs; [
            bashInteractive
            libffi
            python37
            # python37Packages.ansible
            python37Packages.pip
          ];
          buildInputs = [ ];
          shellHook = ''
            # PROJDIR="${toString ./.}}"
            # echo "projdir: $PROJDIR"
            # PROJDIR=$(pwd)
            # echo "projdir: $PROJDIR"
            echo "Using ${pkgs.python37.name}"

            [ ! -d '$PROJDIR/python-dev' ] && python -m venv python-dev && echo "SETUP python-dev: DONE"
            source python-dev/bin/activate
            # python -m pip install --upgrade pip
            python -m pip install -r requirements-dev.txt
            # python -m pip install -r requirements.txt
            python manage.py migrate
            set -a; source .env; set +a
          '';
        };
      });
}

{ sources ? import ./nix/sources.nix
, pkgs ? import sources.nixpkgs {}
}:
pkgs.mkShell {
  nativeBuildInputs = with pkgs; [
    bashInteractive
    libffi
    python38
    # python38Packages.ansible
    python38Packages.pip
    # python38Packages.python-lsp-server
  ];

  shellHook = ''
    echo "Using ${pkgs.python38.name}"

    [ ! -d '$PROJDIR/python-dev' ] && python -m venv python-dev && echo "SETUP python-dev: DONE"
    source python-dev/bin/activate
    python -m pip install -r requirements-dev.txt
    # python -m pip install -r requirements.txt
    python manage.py migrate
    set -a; source .env; set +a
  '';
}

with import <nixpkgs> { };
mkShell {
  nativeBuildInputs = [ bashInteractive python37 python37Packages.pip ansible];

  shellHook = ''
    echo "Using ${python37.name}"

    [ ! -d '$PROJDIR/python-dev' ] && python -m venv python-dev && echo "SETUP python-dev: DONE"
    source python-dev/bin/activate
    python -m pip install -r requirements-dev.txt
    set -a; source .env; set +a
  '';
}

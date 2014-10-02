#!/bin/bash

HELP="NO"
CHECKOUT="HEPFORGE"  # Alternate option is "GITHUB"
REPO="GENIEMC"       # GitHub user account
TAG="R-2_8_4"        # SVN Branch
PYTHIAVER=6          # Must be 6 or 8
MAKE=gmake           # May prefer "make" on Ubuntu
MAKENICE=0           # Run make under nice if == 1
ROOTTAG="v5-34-18"   # 
FORCEBUILD="NO"      # " -f" will archive existing packages and rebuild
HTTPSCHECKOUT=0      # use https checkout if non-zero (otherwise ssh)


# Print the help menu and then exit.
help()
{
  echo ""
  echo ""
  echo "Welcome to rub_the_lamp. This script will build the 3rd party support"
  echo "packages for GENIE and then build GENIE itself. There are MANDATORY"
  echo "options you must supply."
  echo ""
  echo "Usage: ./rub_the_lamp.sh -<flag>"
  echo "             -h / --help   : Help"
  echo "             -g / --github : Check out GENIE code from GitHub"
  echo "             -f / --forge  : Check out GENIE code from HepForge"
  echo "                             (DEFAULT)"
  echo "             -r / --repo   : Specify the GitHub repo"
  echo "                             (default == GENIEMC)"
  echo "             -t / --tag    : Specify the HepForge SVN tag"
  echo "                             (default == R-2_8_4)"
  echo "             -p / --pythia : Pythia version (6 or 8)"
  echo "                             (default == 6)"
  echo "             -m / --make   : Use make instead of gmake"
  echo "                             (default == use gmake)"
  echo "             -n / --nice   : Run make under nice"
  echo "                             (default == normal make)"
  echo "             -o / --root   : ROOT tag version"
  echo "                             (default == v5-34-18)"
  echo "             -s / --https  : Use HTTPS checkout from GitHub"
  echo "                             (default is ssh)"
  echo "             -c / --force  : Archive existing packages and rebuild"
  echo "                             (default is to keep the existing area)"
  echo ""
  echo ""

  exit 1
}

#
# Did the user supply any arguments? If no, print help and exit.
#
if [[ $# < 1 ]]; then
  HELP="YES"
fi

echo ""
echo "Letting GENIE out of the bottle..."
#
# Parse the command line flags.
#
while [[ $# > 0 ]]
do
  key="$1"
  shift

  case $key in
    -h|--help)
    HELP="YES"
    ;;
    -g|--github)
    CHECKOUT="GITHUB"
    ;;
    -f|--forge)
    CHECKOUT="HEPFORGE"
    ;;
    -r|--repo)
    REPO="$1"
    CHECKOUT="GITHUB"
    shift
    ;;
    -t|--tag)
    TAG="$1"
    CHECKOUT="HEPFORGE"
    shift
    ;;
    -p|--pythia)
    PYTHIAVER="$1"
    shift
    ;;
    -m|--make)
    MAKE=make
    ;;
    -n|--nice)
    MAKENICE=1
    ;;
    -o|root)
    ROOTTAG="$1"
    shift
    ;;
    -s|--https)
    HTTPSCHECKOUT=1
    ;;
    -c|--force)
    FORCEBUILD="YES"
    ;;
    *)    # Unknown option

    ;;
  esac
done

if [[ $HELP == "YES" ]]; then
  help
fi

# 
# Show the selected options.
#
echo ""
echo "Options set: "
echo "------------ "
echo " Checkout       = $CHECKOUT"
if [[ $CHECKOUT == "HEPFORGE" ]]; then
  echo " Tag            = $TAG"
elif [[ $CHECKOUT == "GITHUB" ]]; then
  echo " Repo           = $REPO"
  echo " HTTPS Checkout = $HTTPSCHECKOUT"
else
  echo "Bad checkout option!"
  exit 1
fi
echo " Pythia version = $PYTHIAVER"
echo " Make           = $MAKE"
echo " Make Nice      = $MAKENICE"
echo " ROOT tag       = $ROOTTAG"
echo " Force build    = $FORCEBUILD"

# 
# Pause here to verify selection?
# 
echo ""
echo "Press enter to continue or enter any character to quit."
read CONTINUE
if [[ $CONTINUE != "" ]]; then
  echo " Halting!"
fi

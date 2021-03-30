import sys
from src.iss import Iss


########################################################################################################################
# Script body
########################################################################################################################
def _requester():
    allowable_arguments = ["loc", "pass", "people"]

    try:
        if (len(sys.argv) == 1) or (sys.argv[1] not in allowable_arguments):
            args = ', '.join([str(elem) for elem in allowable_arguments])
            sys.exit('Empty or unknown mode provided. One of the following arguments are allowed: [' + args + ']')

        iss_station = Iss()
        mode = sys.argv[1]
        getattr(iss_station, 'get_%s' % mode)(sys.argv[2:])
        if iss_station.status:
            print(iss_station.message)
        else:
            sys.exit(iss_station.message)

    except Exception as e:
        sys.exit("General error: " + str(e))

    sys.exit(0)


def runner():
    if __name__ == "__main__":
        _requester()


runner()

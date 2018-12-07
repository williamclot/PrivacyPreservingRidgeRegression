#include <ENCRYPTO_utils/crypto/crypto.h>
#include <ENCRYPTO_utils/parse_options.h>
#include <abycore/aby/abyparty.h>
#include <abycore/circuit/share.h>
#include <abycore/circuit/booleancircuits.h>
#include <abycore/sharing/sharing.h>
#include <cassert>
#include <iomanip>
#include <iostream>

// My Libraries
#include "common/circuit.h"
#include "common/utils.h"

int main(int argc, char** argv) {

	std::cout << "Launching CSP [-]" << std::endl;

	// Hardcoded server role
	e_role role = SERVER;
	uint32_t bitlen = 1, nvals = 9, secparam = 128, nthreads = 1;

	uint16_t port = 7766;
	std::string address = "127.0.0.1";
	std::string circuit = "none.aby";
	int32_t test_op = -1;
	e_mt_gen_alg mt_alg = MT_OT;
	uint32_t test_bit = 0;

	// Reading options
	read_test_options(&argc, &argv, &role, &bitlen, &nvals, &secparam, &address,
		&port, &test_op, &test_bit, &circuit);

	// Reading the inputs in the /input folder and parsing them in a std::vector
	std::vector<double> csp_data;
	csp_data = get_input("../input/CSP");
	print_vector(csp_data, nvals, "Opening CSP data...");

	seclvl seclvl = get_sec_lvl(secparam);

	test_circuit(role, address, port, seclvl, nvals, nthreads, mt_alg, S_BOOL, csp_data);

	return 0;
}
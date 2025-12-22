#ifndef __PHI_COUPLED__
#define __PHI_COUPLED__

#define _phi_coupled_num_params_ 5

enum {
  phi_coupled_beta_g,
  phi_coupled_beta_gamma,
  phi_coupled_lambda,
  phi_coupled_V0,
  phi_coupled_phi_initial
};

int phi_coupled_background_init(struct background * pba);

#endif

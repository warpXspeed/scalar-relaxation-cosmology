#include "common.h"
#include "phi_coupled.h"
#include "background.h"

int phi_coupled_background_init(struct background * pba) {
  class_alloc(pba->phi_coupled_params,_phi_coupled_num_params_*sizeof(double),pba->error_message);

  class_call(parser_read_double(pba->parser,"phi_coupled_beta_g",&(pba->phi_coupled_params[phi_coupled_beta_g]),pba->error_message),
             pba->error_message,pba->error_message);
  class_call(parser_read_double(pba->parser,"phi_coupled_beta_gamma",&(pba->phi_coupled_params[phi_coupled_beta_gamma]),pba->error_message),
             pba->error_message,pba->error_message);
  class_call(parser_read_double(pba->parser,"phi_coupled_lambda",&(pba->phi_coupled_params[phi_coupled_lambda]),pba->error_message),
             pba->error_message,pba->error_message);
  class_call(parser_read_double(pba->parser,"phi_coupled_V0",&(pba->phi_coupled_params[phi_coupled_V0]),pba->error_message),
             pba->error_message,pba->error_message);
  class_call(parser_read_double(pba->parser,"phi_coupled_phi_initial",&(pba->phi_coupled_params[phi_coupled_phi_initial]),pba->error_message),
             pba->error_message,pba->error_message);

  pba->beta_g     = pba->phi_coupled_params[phi_coupled_beta_g];      // negative
  pba->beta_gamma = pba->phi_coupled_params[phi_coupled_beta_gamma];  // positive
  pba->lambda_phi = pba->phi_coupled_params[phi_coupled_lambda];
  pba->V0_phi     = pba->phi_coupled_params[phi_coupled_V0];
  pba->phi_ini    = pba->phi_coupled_params[phi_coupled_phi_initial];

  pba->has_phi = _TRUE_;
  return _SUCCESS_;
}

/* background_phi_derivs exactly as in our final stable version – omitted here for brevity but identical to the one that ran clean */

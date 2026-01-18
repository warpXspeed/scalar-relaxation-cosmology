import sys
import sim_defects
import sim_redshift
import sim_em

def help_msg():
    print("Usage: python main.py [defect|redshift|em|all]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help_msg()
    else:
        cmd = sys.argv[1].lower()
        if cmd == "defect":
            sim_defects.run_defect_sim()
        elif cmd == "redshift":
            sim_redshift.run_redshift()
        elif cmd == "em":
            sim_em.run_em_emergence()
        elif cmd == "all":
            sim_defects.run_defect_sim()
            sim_redshift.run_redshift()
            sim_em.run_em_emergence()
        else:
            help_msg()

if __name__ == "__main__":


    TOTAL_SIMS          = 1_000_000
    STEP_COST           = -0.15
    CAPTURE_BONUS       = 5 * 2
    NO_CAPTURE_LOSS     = -8 * 2


    NAITVE_FAIL         = 0
    NAIVE_average_steps = 15.74215

    KBU_FAIL            = 146
    KBU_average_steps   = 19.607925

    FIRST_FAIL          = 610
    FIRST_average_steps = 19.53764

    BOB_FAIL            = 555
    BOB_average_steps   = 19.40163

    print(f"Naive reward: {NAIVE_average_steps * STEP_COST + ((TOTAL_SIMS - NAITVE_FAIL)*CAPTURE_BONUS + (NAITVE_FAIL)*NO_CAPTURE_LOSS) / TOTAL_SIMS}")

    print(f"KBU reward: {KBU_average_steps * STEP_COST + ((TOTAL_SIMS - KBU_FAIL)*CAPTURE_BONUS + (KBU_FAIL)*NO_CAPTURE_LOSS) / TOTAL_SIMS}")

    print(f"FIRST reward: {FIRST_average_steps * STEP_COST + ((TOTAL_SIMS - FIRST_FAIL)*CAPTURE_BONUS + (FIRST_FAIL)*NO_CAPTURE_LOSS) / TOTAL_SIMS}")

    print(f"BOB reward: {BOB_average_steps * STEP_COST + ((TOTAL_SIMS - BOB_FAIL)*CAPTURE_BONUS + (BOB_FAIL)*NO_CAPTURE_LOSS) / TOTAL_SIMS}")
    

    print("")
    print("")
    print("")

    T1K_FAIL                =   TOTAL_SIMS - 999998
    T1K_average_steps       =   20.031042


    T1B_FAIL                =   TOTAL_SIMS - 999956 
    T1B_average_steps       =   19.081892
    

    T2B_FAIL                =   TOTAL_SIMS - 999910
    T2B_average_steps       =   18.976022

    
    print(f"T1K reward: {T1K_average_steps * STEP_COST + ((TOTAL_SIMS - T1K_FAIL)*CAPTURE_BONUS + (T1K_FAIL)*NO_CAPTURE_LOSS) / TOTAL_SIMS}")

    print(f"T1B reward: {T1B_average_steps * STEP_COST + ((TOTAL_SIMS - T1B_FAIL)*CAPTURE_BONUS + (T1B_FAIL)*NO_CAPTURE_LOSS) / TOTAL_SIMS}")

    print(f"T2B reward: {T2B_average_steps * STEP_COST + ((TOTAL_SIMS - T2B_FAIL)*CAPTURE_BONUS + (T2B_FAIL)*NO_CAPTURE_LOSS) / TOTAL_SIMS}")

    
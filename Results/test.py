if __name__ == "__main__":


    TOTAL_SIMS          = 1_000_000
    STEP_COST           = -0.15
    CAPTURE_BONUS       = 5 * 2
    NO_CAPTURE_LOSS     = -8 * 2


    NAITVE_FAIL         = 5158
    NAIVE_average_steps =  19.717877

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


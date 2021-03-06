import subprocess

benchmarks = ['merge', 'lfsr', 'mm', 'sieve', 'spmv']
cache_repls = ['LIPRP', 'NMRURP', 'RandomRP']

for prog_name in benchmarks:
    prog_loc = "../cs251a-microbench/" + prog_name
    for repl in cache_repls:
        freq = "2.2GHz"
        inst = ("../gem5/build/X86/gem5.opt --outdir=policy_tests_%s ../gem5/configs/example/se.py --cmd=%s --cpu-type=DerivO3CPU " +\
        "--cpu-clock=%s --caches --l1d_size=64kB --l1i_size=64kB --l2cache --l2_size=2MB --mem-type=DDR3_1600_8x8 " +\
        "--l1d_repl=%s --l2_repl=%s --l1d_assoc=%s --l2_assoc=%s")
        inst = inst % (prog_name, repl, prog_loc, freq, repl, repl, 4, 4)
        subprocess.run(inst.split()) 

Quadratic Programming based Absolute Policy Optimization: qpAPO

our qpAPO is a variant of absolute policy optimization (APO) and rTRPO is a variant of TRPO, which are coded according to the codding style of APO software package:  https://github.com/intelligent-control-lab/Absolute-Policy-Optimization

This package also includes five existing RL methods (APO, PAPO, ESPO, TRPO, PPO), which directly come from APO software package: https://github.com/intelligent-control-lab/Absolute-Policy-Optimization

APO and PAPO
Weiye Zhao, Feihan Li, Yifan Sun, Rui Chen, Tianhao Wei, Changliu Liu. Absolute Policy Optimization: Enhancing Lower Probability Bound of Performance with High Confidence. ICML-2024, pp. 60866-60905.

ESPO
Mingfei Sun, Vitaly Kurin, Guoqing Liu, Sam Devlin, Tao Qin, Katja Hofmann, Shimon Whiteson. You May Not Need Ratio Clipping in PPO. arXiv:2202.00079v1, 2022

TRPO
John Schulman, Sergey Levine, Pieter Abbeel, Michael Jordan, Philipp Moritz. Trust Region Policy Optimization. ICML 2015, pp. 1889-1897.

PPO: 
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov. Proximal Policy Optimization Algorithms. arXiv:1707.06347v2, 2017.

rTRPO:
Haotian Xu, Junyu Xuan, Guangquan Zhang, and Jie Lu. Reciprocal Trust Region Policy Optimization. FLINS-ISKE, 2024, pp. 187-194.

our running results are stored in the subfold: Results/env/env_agent/xxx.csv

In Results/env, we provide a matlab function to draw a figure for each environment.










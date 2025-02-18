# Copyright 2022 MetaOPT Team. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""object oriented optimizer implementations."""

from torchopt.optim import meta
from torchopt.optim.adam import Adam
from torchopt.optim.adamw import AdamW
from torchopt.optim.base import Optimizer
from torchopt.optim.func import FuncOptimizer
from torchopt.optim.rmsprop import RMSProp, RMSprop
from torchopt.optim.sgd import SGD

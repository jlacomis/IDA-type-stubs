from enum import auto, Enum
from typing import Any, List

from ida_typeinf import tinfo_t

class DecompilationFailure(Exception):
    pass

# This is technically cfuncptr_t, but that is just a reference-counted
# version of cfunc_t
def decompile(*args) -> cfunc_t: ...
def get_hexrays_version() -> str: ...
def init_hexrays_plugin() -> bool: ...
def load_plugin(name: str) -> None: ...

class ctype_t:
    pass

class cot_empty(ctype_t):
    pass

class cot_comma(ctype_t):
    pass

class cot_asg(ctype_t):
    pass

class cot_asgbor(ctype_t):
    pass

class cot_asgxor(ctype_t):
    pass

class cot_asgband(ctype_t):
    pass

class cot_asgadd(ctype_t):
    pass

class cot_asgsub(ctype_t):
    pass

class cot_asgmul(ctype_t):
    pass

class cot_asgsshr(ctype_t):
    pass

class cot_asgushr(ctype_t):
    pass

class cot_asgshl(ctype_t):
    pass

class cot_asgsdiv(ctype_t):
    pass

class cot_asgudiv(ctype_t):
    pass

class cot_asgsmod(ctype_t):
    pass

class cot_asgumod(ctype_t):
    pass

class cot_tern(ctype_t):
    pass

class cot_lor(ctype_t):
    pass

class cot_land(ctype_t):
    pass

class cot_bor(ctype_t):
    pass

class cot_xor(ctype_t):
    pass

class cot_band(ctype_t):
    pass

class cot_eq(ctype_t):
    pass

class cot_ne(ctype_t):
    pass

class cot_sge(ctype_t):
    pass

class cot_uge(ctype_t):
    pass

class cot_sle(ctype_t):
    pass

class cot_ule(ctype_t):
    pass

class cot_sgt(ctype_t):
    pass

class cot_ugt(ctype_t):
    pass

class cot_slt(ctype_t):
    pass

class cot_ult(ctype_t):
    pass

class cot_sshr(ctype_t):
    pass

class cot_ushr(ctype_t):
    pass

class cot_shl(ctype_t):
    pass

class cot_add(ctype_t):
    pass

class cot_sub(ctype_t):
    pass

class cot_mul(ctype_t):
    pass

class cot_sdiv(ctype_t):
    pass

class cot_udiv(ctype_t):
    pass

class cot_smod(ctype_t):
    pass

class cot_umod(ctype_t):
    pass

class cot_fadd(ctype_t):
    pass

class cot_fsub(ctype_t):
    pass

class cot_fmul(ctype_t):
    pass

class cot_fdiv(ctype_t):
    pass

class cot_fneg(ctype_t):
    pass

class cot_neg(ctype_t):
    pass

class cot_cast(ctype_t):
    pass

class cot_lnot(ctype_t):
    pass

class cot_bnot(ctype_t):
    pass

class cot_ptr(ctype_t):
    pass

class cot_ref(ctype_t):
    pass

class cot_postinc(ctype_t):
    pass

class cot_postdec(ctype_t):
    pass

class cot_preinc(ctype_t):
    pass

class cot_predec(ctype_t):
    pass

class cot_call(ctype_t):
    pass

class cot_idx(ctype_t):
    pass

class cot_memref(ctype_t):
    pass

class cot_memptr(ctype_t):
    pass

class cot_num(ctype_t):
    pass

class cot_fnum(ctype_t):
    pass

class cot_str(ctype_t):
    pass

class cot_obj(ctype_t):
    pass

class cot_var(ctype_t):
    pass

class cot_insn(ctype_t):
    pass

class cot_sizeof(ctype_t):
    pass

class cot_helper(ctype_t):
    pass

class cot_type(ctype_t):
    pass

class cot_last(ctype_t):
    pass

class cit_empty(ctype_t):
    pass

class cit_block(ctype_t):
    pass

class cit_expr(ctype_t):
    pass

class cit_if(ctype_t):
    pass

class cit_for(ctype_t):
    pass

class cit_while(ctype_t):
    pass

class cit_do(ctype_t):
    pass

class cit_switch(ctype_t):
    pass

class cit_break(ctype_t):
    pass

class cit_continue(ctype_t):
    pass

class cit_return(ctype_t):
    pass

class cit_goto(ctype_t):
    pass

class cit_asm(ctype_t):
    pass

class cit_end(ctype_t):
    pass

class citem_t:
    ea: int
    obj_id: int
    op: "ctype_t"


class cexpr_t(citem_t):
    a: List[Any]
    fpc: "fnumber_t"
    insn: "cinsn_t"
    m: int
    n: int
    obj_ea: int
    ptrsize: int
    string: str
    type: tinfo_t
    v: "var_ref_t"
    x: "cexpr_t"
    y: "cexpr_t"
    z: "cexpr_t"


class cinsn_t(citem_t):
    cblock: "cblock_t"
    cexpr: "cexpr_t"
    cif: "cif_t"
    cfor: "cfor_t"
    cwhile: "cwhile_t"
    cdo: "cdo_t"
    cswitch: "cswitch_t"
    creturn: "creturn_t"
    cgoto: "cgoto_t"
    casm: "casm_t"

class ceinsn_t:
    obj_id: int
    expr: "cexpr_t"

class var_ref_t:
    mba: Any
    idx: int

class fnumber_t:
    fnum: int
    nbytes: int

class qlist_cinsn_t(list):
    # list is technically a lie
    pass

class cblock_t(qlist_cinsn_t):
    obj_id: int

class cif_t(ceinsn_t):
    ithen: "cinsn_t"
    ielse: "cinsn_t"

class cloop_t(ceinsn_t):
    body: "cinsn_t"

class cdo_t(cloop_t):
    pass

class cfor_t(cloop_t):
    init: "cexpr_t"
    step: "cexpr_t"

class cwhile_t(cloop_t):
    pass

class cnumber_t:
    def value(self, typ: tinfo_t) -> int: ...

class ccase_t(cinsn_t):
    values: List[int]
    def size(self) -> int: ...
    def value(self, i: int) -> int: ...

class cswitch_t(ceinsn_t):
    mvnf: "cnumber_t"
    cases: List["ccase_t"]

class creturn_t(ceinsn_t):
    pass

class cgoto_t:
    obj_id: int
    label_num: int

class casm_t:
    obj_id: int

class carg_t(cexpr_t):
    is_vararg: bool
    formal_type: tinfo_t

class lvar_locator_t:
    def get_stkoff(self) -> int: ...
    def get_reg1(self) -> int: ...
    def get_reg2(self) -> int: ...
    def is_reg1(self) -> bool: ...
    def is_reg2(self) -> bool: ...
    def is_reg_var(self) -> bool: ...
    def is_stk_var(self) -> bool: ...

class lvar_t(lvar_locator_t):
    name: str

    @property
    def is_arg_var(self) -> bool: ...

    @property
    def has_user_name(self) -> bool: ...
    def type(self) -> "tinfo_t": ...

class cfunc_t:
    arguments: List["lvar_t"]
    lvars: List["lvar_t"]
    body: "cblock_t"
    type: tinfo_t

    def get_lvars(self) -> List["lvar_t"]: ...
    def get_stkoff_delta(self) -> int: ...

class ctree_visitor_t:
    def leave_insn(self, *args) -> int: ...
    def leave_expr(self, *args) -> int: ...
    def parent_insn(self, *args) -> "cinsn_t": ...
    def parent_expr(self, *args) -> "cexpr_t": ...

class ctree_parentee_t(ctree_visitor_t):
    pass

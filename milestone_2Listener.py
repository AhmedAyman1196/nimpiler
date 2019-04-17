# Generated from milestone_2.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .milestone_2Parser import milestone_2Parser
else:
    from milestone_2Parser import milestone_2Parser

# This class defines a complete listener for a parse tree produced by milestone_2Parser.
class milestone_2Listener(ParseTreeListener):

    # Enter a parse tree produced by milestone_2Parser#module.
    def enterModule(self, ctx:milestone_2Parser.ModuleContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#module.
    def exitModule(self, ctx:milestone_2Parser.ModuleContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#comma.
    def enterComma(self, ctx:milestone_2Parser.CommaContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#comma.
    def exitComma(self, ctx:milestone_2Parser.CommaContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#semicolon.
    def enterSemicolon(self, ctx:milestone_2Parser.SemicolonContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#semicolon.
    def exitSemicolon(self, ctx:milestone_2Parser.SemicolonContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#colon.
    def enterColon(self, ctx:milestone_2Parser.ColonContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#colon.
    def exitColon(self, ctx:milestone_2Parser.ColonContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#colcom.
    def enterColcom(self, ctx:milestone_2Parser.ColcomContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#colcom.
    def exitColcom(self, ctx:milestone_2Parser.ColcomContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#operator.
    def enterOperator(self, ctx:milestone_2Parser.OperatorContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#operator.
    def exitOperator(self, ctx:milestone_2Parser.OperatorContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#prefixOperator.
    def enterPrefixOperator(self, ctx:milestone_2Parser.PrefixOperatorContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#prefixOperator.
    def exitPrefixOperator(self, ctx:milestone_2Parser.PrefixOperatorContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#optInd.
    def enterOptInd(self, ctx:milestone_2Parser.OptIndContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#optInd.
    def exitOptInd(self, ctx:milestone_2Parser.OptIndContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#optPar.
    def enterOptPar(self, ctx:milestone_2Parser.OptParContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#optPar.
    def exitOptPar(self, ctx:milestone_2Parser.OptParContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#symbol.
    def enterSymbol(self, ctx:milestone_2Parser.SymbolContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#symbol.
    def exitSymbol(self, ctx:milestone_2Parser.SymbolContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#exprColonEqExpr.
    def enterExprColonEqExpr(self, ctx:milestone_2Parser.ExprColonEqExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#exprColonEqExpr.
    def exitExprColonEqExpr(self, ctx:milestone_2Parser.ExprColonEqExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#exprList.
    def enterExprList(self, ctx:milestone_2Parser.ExprListContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#exprList.
    def exitExprList(self, ctx:milestone_2Parser.ExprListContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#exprColonEqExprList.
    def enterExprColonEqExprList(self, ctx:milestone_2Parser.ExprColonEqExprListContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#exprColonEqExprList.
    def exitExprColonEqExprList(self, ctx:milestone_2Parser.ExprColonEqExprListContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#dotExpr.
    def enterDotExpr(self, ctx:milestone_2Parser.DotExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#dotExpr.
    def exitDotExpr(self, ctx:milestone_2Parser.DotExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#explicitGenericInstantiation.
    def enterExplicitGenericInstantiation(self, ctx:milestone_2Parser.ExplicitGenericInstantiationContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#explicitGenericInstantiation.
    def exitExplicitGenericInstantiation(self, ctx:milestone_2Parser.ExplicitGenericInstantiationContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#qualifiedIdent.
    def enterQualifiedIdent(self, ctx:milestone_2Parser.QualifiedIdentContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#qualifiedIdent.
    def exitQualifiedIdent(self, ctx:milestone_2Parser.QualifiedIdentContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#setOrTableConstr.
    def enterSetOrTableConstr(self, ctx:milestone_2Parser.SetOrTableConstrContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#setOrTableConstr.
    def exitSetOrTableConstr(self, ctx:milestone_2Parser.SetOrTableConstrContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#castExpr.
    def enterCastExpr(self, ctx:milestone_2Parser.CastExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#castExpr.
    def exitCastExpr(self, ctx:milestone_2Parser.CastExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#parKeyw.
    def enterParKeyw(self, ctx:milestone_2Parser.ParKeywContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#parKeyw.
    def exitParKeyw(self, ctx:milestone_2Parser.ParKeywContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#exprColonExpr.
    def enterExprColonExpr(self, ctx:milestone_2Parser.ExprColonExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#exprColonExpr.
    def exitExprColonExpr(self, ctx:milestone_2Parser.ExprColonExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#literal.
    def enterLiteral(self, ctx:milestone_2Parser.LiteralContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#literal.
    def exitLiteral(self, ctx:milestone_2Parser.LiteralContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#generalizedLit.
    def enterGeneralizedLit(self, ctx:milestone_2Parser.GeneralizedLitContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#generalizedLit.
    def exitGeneralizedLit(self, ctx:milestone_2Parser.GeneralizedLitContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#identOrLiteral.
    def enterIdentOrLiteral(self, ctx:milestone_2Parser.IdentOrLiteralContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#identOrLiteral.
    def exitIdentOrLiteral(self, ctx:milestone_2Parser.IdentOrLiteralContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#tupleConstr.
    def enterTupleConstr(self, ctx:milestone_2Parser.TupleConstrContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#tupleConstr.
    def exitTupleConstr(self, ctx:milestone_2Parser.TupleConstrContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#arrayConstr.
    def enterArrayConstr(self, ctx:milestone_2Parser.ArrayConstrContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#arrayConstr.
    def exitArrayConstr(self, ctx:milestone_2Parser.ArrayConstrContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#primarySuffix.
    def enterPrimarySuffix(self, ctx:milestone_2Parser.PrimarySuffixContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#primarySuffix.
    def exitPrimarySuffix(self, ctx:milestone_2Parser.PrimarySuffixContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#indexExprList.
    def enterIndexExprList(self, ctx:milestone_2Parser.IndexExprListContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#indexExprList.
    def exitIndexExprList(self, ctx:milestone_2Parser.IndexExprListContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#pragmas.
    def enterPragmas(self, ctx:milestone_2Parser.PragmasContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#pragmas.
    def exitPragmas(self, ctx:milestone_2Parser.PragmasContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#indentWithPragma.
    def enterIndentWithPragma(self, ctx:milestone_2Parser.IndentWithPragmaContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#indentWithPragma.
    def exitIndentWithPragma(self, ctx:milestone_2Parser.IndentWithPragmaContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#caseExpr.
    def enterCaseExpr(self, ctx:milestone_2Parser.CaseExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#caseExpr.
    def exitCaseExpr(self, ctx:milestone_2Parser.CaseExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#typeDescK.
    def enterTypeDescK(self, ctx:milestone_2Parser.TypeDescKContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#typeDescK.
    def exitTypeDescK(self, ctx:milestone_2Parser.TypeDescKContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#typeDesc.
    def enterTypeDesc(self, ctx:milestone_2Parser.TypeDescContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#typeDesc.
    def exitTypeDesc(self, ctx:milestone_2Parser.TypeDescContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#macroColon.
    def enterMacroColon(self, ctx:milestone_2Parser.MacroColonContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#macroColon.
    def exitMacroColon(self, ctx:milestone_2Parser.MacroColonContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#moduleName.
    def enterModuleName(self, ctx:milestone_2Parser.ModuleNameContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#moduleName.
    def exitModuleName(self, ctx:milestone_2Parser.ModuleNameContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#sectionTypeDef.
    def enterSectionTypeDef(self, ctx:milestone_2Parser.SectionTypeDefContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#sectionTypeDef.
    def exitSectionTypeDef(self, ctx:milestone_2Parser.SectionTypeDefContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#sectionConstant.
    def enterSectionConstant(self, ctx:milestone_2Parser.SectionConstantContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#sectionConstant.
    def exitSectionConstant(self, ctx:milestone_2Parser.SectionConstantContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#sectionVariable.
    def enterSectionVariable(self, ctx:milestone_2Parser.SectionVariableContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#sectionVariable.
    def exitSectionVariable(self, ctx:milestone_2Parser.SectionVariableContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#exportStmt.
    def enterExportStmt(self, ctx:milestone_2Parser.ExportStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#exportStmt.
    def exitExportStmt(self, ctx:milestone_2Parser.ExportStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#expr.
    def enterExpr(self, ctx:milestone_2Parser.ExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#expr.
    def exitExpr(self, ctx:milestone_2Parser.ExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#typeKeyw.
    def enterTypeKeyw(self, ctx:milestone_2Parser.TypeKeywContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#typeKeyw.
    def exitTypeKeyw(self, ctx:milestone_2Parser.TypeKeywContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#exprStmt.
    def enterExprStmt(self, ctx:milestone_2Parser.ExprStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#exprStmt.
    def exitExprStmt(self, ctx:milestone_2Parser.ExprStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#typeDefAux.
    def enterTypeDefAux(self, ctx:milestone_2Parser.TypeDefAuxContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#typeDefAux.
    def exitTypeDefAux(self, ctx:milestone_2Parser.TypeDefAuxContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#par.
    def enterPar(self, ctx:milestone_2Parser.ParContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#par.
    def exitPar(self, ctx:milestone_2Parser.ParContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#opr.
    def enterOpr(self, ctx:milestone_2Parser.OprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#opr.
    def exitOpr(self, ctx:milestone_2Parser.OprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#doBlocks.
    def enterDoBlocks(self, ctx:milestone_2Parser.DoBlocksContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#doBlocks.
    def exitDoBlocks(self, ctx:milestone_2Parser.DoBlocksContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#p.
    def enterP(self, ctx:milestone_2Parser.PContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#p.
    def exitP(self, ctx:milestone_2Parser.PContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#condExpr.
    def enterCondExpr(self, ctx:milestone_2Parser.CondExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#condExpr.
    def exitCondExpr(self, ctx:milestone_2Parser.CondExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#ifExpr.
    def enterIfExpr(self, ctx:milestone_2Parser.IfExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#ifExpr.
    def exitIfExpr(self, ctx:milestone_2Parser.IfExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#whenExpr.
    def enterWhenExpr(self, ctx:milestone_2Parser.WhenExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#whenExpr.
    def exitWhenExpr(self, ctx:milestone_2Parser.WhenExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#pragma.
    def enterPragma(self, ctx:milestone_2Parser.PragmaContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#pragma.
    def exitPragma(self, ctx:milestone_2Parser.PragmaContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#identVis.
    def enterIdentVis(self, ctx:milestone_2Parser.IdentVisContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#identVis.
    def exitIdentVis(self, ctx:milestone_2Parser.IdentVisContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#identVisDot.
    def enterIdentVisDot(self, ctx:milestone_2Parser.IdentVisDotContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#identVisDot.
    def exitIdentVisDot(self, ctx:milestone_2Parser.IdentVisDotContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#identWithPragma.
    def enterIdentWithPragma(self, ctx:milestone_2Parser.IdentWithPragmaContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#identWithPragma.
    def exitIdentWithPragma(self, ctx:milestone_2Parser.IdentWithPragmaContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#identWithPragmaDot.
    def enterIdentWithPragmaDot(self, ctx:milestone_2Parser.IdentWithPragmaDotContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#identWithPragmaDot.
    def exitIdentWithPragmaDot(self, ctx:milestone_2Parser.IdentWithPragmaDotContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#declColonEquals.
    def enterDeclColonEquals(self, ctx:milestone_2Parser.DeclColonEqualsContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#declColonEquals.
    def exitDeclColonEquals(self, ctx:milestone_2Parser.DeclColonEqualsContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#identColonEquals.
    def enterIdentColonEquals(self, ctx:milestone_2Parser.IdentColonEqualsContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#identColonEquals.
    def exitIdentColonEquals(self, ctx:milestone_2Parser.IdentColonEqualsContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#inlTupleDecl.
    def enterInlTupleDecl(self, ctx:milestone_2Parser.InlTupleDeclContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#inlTupleDecl.
    def exitInlTupleDecl(self, ctx:milestone_2Parser.InlTupleDeclContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#extTupleDecl.
    def enterExtTupleDecl(self, ctx:milestone_2Parser.ExtTupleDeclContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#extTupleDecl.
    def exitExtTupleDecl(self, ctx:milestone_2Parser.ExtTupleDeclContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#tupleClass.
    def enterTupleClass(self, ctx:milestone_2Parser.TupleClassContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#tupleClass.
    def exitTupleClass(self, ctx:milestone_2Parser.TupleClassContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#paramList.
    def enterParamList(self, ctx:milestone_2Parser.ParamListContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#paramList.
    def exitParamList(self, ctx:milestone_2Parser.ParamListContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#paramListArrow.
    def enterParamListArrow(self, ctx:milestone_2Parser.ParamListArrowContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#paramListArrow.
    def exitParamListArrow(self, ctx:milestone_2Parser.ParamListArrowContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#paramListColon.
    def enterParamListColon(self, ctx:milestone_2Parser.ParamListColonContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#paramListColon.
    def exitParamListColon(self, ctx:milestone_2Parser.ParamListColonContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#doBlock.
    def enterDoBlock(self, ctx:milestone_2Parser.DoBlockContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#doBlock.
    def exitDoBlock(self, ctx:milestone_2Parser.DoBlockContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#procExpr.
    def enterProcExpr(self, ctx:milestone_2Parser.ProcExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#procExpr.
    def exitProcExpr(self, ctx:milestone_2Parser.ProcExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#distinct.
    def enterDistinct(self, ctx:milestone_2Parser.DistinctContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#distinct.
    def exitDistinct(self, ctx:milestone_2Parser.DistinctContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#forStmt.
    def enterForStmt(self, ctx:milestone_2Parser.ForStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#forStmt.
    def exitForStmt(self, ctx:milestone_2Parser.ForStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#forExpr.
    def enterForExpr(self, ctx:milestone_2Parser.ForExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#forExpr.
    def exitForExpr(self, ctx:milestone_2Parser.ForExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#primary.
    def enterPrimary(self, ctx:milestone_2Parser.PrimaryContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#primary.
    def exitPrimary(self, ctx:milestone_2Parser.PrimaryContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#importStmt.
    def enterImportStmt(self, ctx:milestone_2Parser.ImportStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#importStmt.
    def exitImportStmt(self, ctx:milestone_2Parser.ImportStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#includeStmt.
    def enterIncludeStmt(self, ctx:milestone_2Parser.IncludeStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#includeStmt.
    def exitIncludeStmt(self, ctx:milestone_2Parser.IncludeStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#fromStmt.
    def enterFromStmt(self, ctx:milestone_2Parser.FromStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#fromStmt.
    def exitFromStmt(self, ctx:milestone_2Parser.FromStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#returnStmt.
    def enterReturnStmt(self, ctx:milestone_2Parser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#returnStmt.
    def exitReturnStmt(self, ctx:milestone_2Parser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#raiseStmt.
    def enterRaiseStmt(self, ctx:milestone_2Parser.RaiseStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#raiseStmt.
    def exitRaiseStmt(self, ctx:milestone_2Parser.RaiseStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#yieldStmt.
    def enterYieldStmt(self, ctx:milestone_2Parser.YieldStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#yieldStmt.
    def exitYieldStmt(self, ctx:milestone_2Parser.YieldStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#discardStmt.
    def enterDiscardStmt(self, ctx:milestone_2Parser.DiscardStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#discardStmt.
    def exitDiscardStmt(self, ctx:milestone_2Parser.DiscardStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#breakStmt.
    def enterBreakStmt(self, ctx:milestone_2Parser.BreakStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#breakStmt.
    def exitBreakStmt(self, ctx:milestone_2Parser.BreakStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#continueStmt.
    def enterContinueStmt(self, ctx:milestone_2Parser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#continueStmt.
    def exitContinueStmt(self, ctx:milestone_2Parser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#condStmt.
    def enterCondStmt(self, ctx:milestone_2Parser.CondStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#condStmt.
    def exitCondStmt(self, ctx:milestone_2Parser.CondStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#ifStmt.
    def enterIfStmt(self, ctx:milestone_2Parser.IfStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#ifStmt.
    def exitIfStmt(self, ctx:milestone_2Parser.IfStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#whenStmt.
    def enterWhenStmt(self, ctx:milestone_2Parser.WhenStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#whenStmt.
    def exitWhenStmt(self, ctx:milestone_2Parser.WhenStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#whileStmt.
    def enterWhileStmt(self, ctx:milestone_2Parser.WhileStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#whileStmt.
    def exitWhileStmt(self, ctx:milestone_2Parser.WhileStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#ofBranch.
    def enterOfBranch(self, ctx:milestone_2Parser.OfBranchContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#ofBranch.
    def exitOfBranch(self, ctx:milestone_2Parser.OfBranchContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#ofBranches.
    def enterOfBranches(self, ctx:milestone_2Parser.OfBranchesContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#ofBranches.
    def exitOfBranches(self, ctx:milestone_2Parser.OfBranchesContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#caseStmt.
    def enterCaseStmt(self, ctx:milestone_2Parser.CaseStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#caseStmt.
    def exitCaseStmt(self, ctx:milestone_2Parser.CaseStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#tryStmt.
    def enterTryStmt(self, ctx:milestone_2Parser.TryStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#tryStmt.
    def exitTryStmt(self, ctx:milestone_2Parser.TryStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#tryExpr.
    def enterTryExpr(self, ctx:milestone_2Parser.TryExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#tryExpr.
    def exitTryExpr(self, ctx:milestone_2Parser.TryExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#exceptBlock.
    def enterExceptBlock(self, ctx:milestone_2Parser.ExceptBlockContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#exceptBlock.
    def exitExceptBlock(self, ctx:milestone_2Parser.ExceptBlockContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#blockStmt.
    def enterBlockStmt(self, ctx:milestone_2Parser.BlockStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#blockStmt.
    def exitBlockStmt(self, ctx:milestone_2Parser.BlockStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#blockExpr.
    def enterBlockExpr(self, ctx:milestone_2Parser.BlockExprContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#blockExpr.
    def exitBlockExpr(self, ctx:milestone_2Parser.BlockExprContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#staticStmt.
    def enterStaticStmt(self, ctx:milestone_2Parser.StaticStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#staticStmt.
    def exitStaticStmt(self, ctx:milestone_2Parser.StaticStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#deferStmt.
    def enterDeferStmt(self, ctx:milestone_2Parser.DeferStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#deferStmt.
    def exitDeferStmt(self, ctx:milestone_2Parser.DeferStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#asmStmt.
    def enterAsmStmt(self, ctx:milestone_2Parser.AsmStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#asmStmt.
    def exitAsmStmt(self, ctx:milestone_2Parser.AsmStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#genericParam.
    def enterGenericParam(self, ctx:milestone_2Parser.GenericParamContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#genericParam.
    def exitGenericParam(self, ctx:milestone_2Parser.GenericParamContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#genericParamList.
    def enterGenericParamList(self, ctx:milestone_2Parser.GenericParamListContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#genericParamList.
    def exitGenericParamList(self, ctx:milestone_2Parser.GenericParamListContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#pattern.
    def enterPattern(self, ctx:milestone_2Parser.PatternContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#pattern.
    def exitPattern(self, ctx:milestone_2Parser.PatternContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#indAndComment.
    def enterIndAndComment(self, ctx:milestone_2Parser.IndAndCommentContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#indAndComment.
    def exitIndAndComment(self, ctx:milestone_2Parser.IndAndCommentContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#routine.
    def enterRoutine(self, ctx:milestone_2Parser.RoutineContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#routine.
    def exitRoutine(self, ctx:milestone_2Parser.RoutineContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#commentStmt.
    def enterCommentStmt(self, ctx:milestone_2Parser.CommentStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#commentStmt.
    def exitCommentStmt(self, ctx:milestone_2Parser.CommentStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#sectionp.
    def enterSectionp(self, ctx:milestone_2Parser.SectionpContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#sectionp.
    def exitSectionp(self, ctx:milestone_2Parser.SectionpContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#constant.
    def enterConstant(self, ctx:milestone_2Parser.ConstantContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#constant.
    def exitConstant(self, ctx:milestone_2Parser.ConstantContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#enum.
    def enterEnum(self, ctx:milestone_2Parser.EnumContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#enum.
    def exitEnum(self, ctx:milestone_2Parser.EnumContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#objectWhen.
    def enterObjectWhen(self, ctx:milestone_2Parser.ObjectWhenContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#objectWhen.
    def exitObjectWhen(self, ctx:milestone_2Parser.ObjectWhenContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#objectBranch.
    def enterObjectBranch(self, ctx:milestone_2Parser.ObjectBranchContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#objectBranch.
    def exitObjectBranch(self, ctx:milestone_2Parser.ObjectBranchContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#objectBranches.
    def enterObjectBranches(self, ctx:milestone_2Parser.ObjectBranchesContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#objectBranches.
    def exitObjectBranches(self, ctx:milestone_2Parser.ObjectBranchesContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#objectCase.
    def enterObjectCase(self, ctx:milestone_2Parser.ObjectCaseContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#objectCase.
    def exitObjectCase(self, ctx:milestone_2Parser.ObjectCaseContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#objectPart.
    def enterObjectPart(self, ctx:milestone_2Parser.ObjectPartContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#objectPart.
    def exitObjectPart(self, ctx:milestone_2Parser.ObjectPartContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#objectX.
    def enterObjectX(self, ctx:milestone_2Parser.ObjectXContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#objectX.
    def exitObjectX(self, ctx:milestone_2Parser.ObjectXContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#typeClassParam.
    def enterTypeClassParam(self, ctx:milestone_2Parser.TypeClassParamContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#typeClassParam.
    def exitTypeClassParam(self, ctx:milestone_2Parser.TypeClassParamContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#typeClass.
    def enterTypeClass(self, ctx:milestone_2Parser.TypeClassContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#typeClass.
    def exitTypeClass(self, ctx:milestone_2Parser.TypeClassContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#typeDef.
    def enterTypeDef(self, ctx:milestone_2Parser.TypeDefContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#typeDef.
    def exitTypeDef(self, ctx:milestone_2Parser.TypeDefContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#varTuple.
    def enterVarTuple(self, ctx:milestone_2Parser.VarTupleContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#varTuple.
    def exitVarTuple(self, ctx:milestone_2Parser.VarTupleContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#colonBody.
    def enterColonBody(self, ctx:milestone_2Parser.ColonBodyContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#colonBody.
    def exitColonBody(self, ctx:milestone_2Parser.ColonBodyContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#variable.
    def enterVariable(self, ctx:milestone_2Parser.VariableContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#variable.
    def exitVariable(self, ctx:milestone_2Parser.VariableContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#bindStmt.
    def enterBindStmt(self, ctx:milestone_2Parser.BindStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#bindStmt.
    def exitBindStmt(self, ctx:milestone_2Parser.BindStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#mixinStmt.
    def enterMixinStmt(self, ctx:milestone_2Parser.MixinStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#mixinStmt.
    def exitMixinStmt(self, ctx:milestone_2Parser.MixinStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#pragmaStmt.
    def enterPragmaStmt(self, ctx:milestone_2Parser.PragmaStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#pragmaStmt.
    def exitPragmaStmt(self, ctx:milestone_2Parser.PragmaStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#simpleStmt.
    def enterSimpleStmt(self, ctx:milestone_2Parser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#simpleStmt.
    def exitSimpleStmt(self, ctx:milestone_2Parser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#complexOrSimpleStmt.
    def enterComplexOrSimpleStmt(self, ctx:milestone_2Parser.ComplexOrSimpleStmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#complexOrSimpleStmt.
    def exitComplexOrSimpleStmt(self, ctx:milestone_2Parser.ComplexOrSimpleStmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#stmt.
    def enterStmt(self, ctx:milestone_2Parser.StmtContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#stmt.
    def exitStmt(self, ctx:milestone_2Parser.StmtContext):
        pass


    # Enter a parse tree produced by milestone_2Parser#start.
    def enterStart(self, ctx:milestone_2Parser.StartContext):
        pass

    # Exit a parse tree produced by milestone_2Parser#start.
    def exitStart(self, ctx:milestone_2Parser.StartContext):
        pass



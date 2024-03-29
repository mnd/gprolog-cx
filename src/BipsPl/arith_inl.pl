/*-------------------------------------------------------------------------*
 * GNU Prolog                                                              *
 *                                                                         *
 * Part  : Prolog buit-in predicates                                       *
 * File  : arith_inl.pl                                                    *
 * Descr.: arithmetic (inline) management - defs for meta-call             *
 * Author: Daniel Diaz                                                     *
 *                                                                         *
 * Copyright (C) 1999-2012 Daniel Diaz                                     *
 *                                                                         *
 * This file is part of GNU Prolog                                         *
 *                                                                         *
 * GNU Prolog is free software: you can redistribute it and/or             *
 * modify it under the terms of either:                                    *
 *                                                                         *
 *   - the GNU Lesser General Public License as published by the Free      *
 *     Software Foundation; either version 3 of the License, or (at your   *
 *     option) any later version.                                          *
 *                                                                         *
 * or                                                                      *
 *                                                                         *
 *   - the GNU General Public License as published by the Free             *
 *     Software Foundation; either version 2 of the License, or (at your   *
 *     option) any later version.                                          *
 *                                                                         *
 * or both in parallel, as here.                                           *
 *                                                                         *
 * GNU Prolog is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of          *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU       *
 * General Public License for more details.                                *
 *                                                                         *
 * You should have received copies of the GNU General Public License and   *
 * the GNU Lesser General Public License along with this program.  If      *
 * not, see http://www.gnu.org/licenses/.                                  *
 *-------------------------------------------------------------------------*/

/* $Id: arith_inl.pl,v 1.19 2012/04/30 16:11:48 diaz Exp $ */

:-	built_in.

'$use_arith_inl'.


X is Y :-
	X is Y.

X =:= Y :-
	X =:= Y.

X =\= Y :-
	X =\= Y.

X < Y :-
	X < Y.

X =< Y :-
	X =< Y.

X > Y :-
	X > Y.

X >= Y :-
	X >= Y.


'$arith_eval'(X, Y) :-
	'$call_c'('Pl_Arith_Eval_2'(X, Y)).


succ(X, Y) :-
	set_bip_name(succ, 2),
	'$call_c_test'('Pl_Succ_2'(X, Y)).


'Simple conditional (only do something if condition is true)
If (<condition_to_evaluate>) Then
    <things_to_do_if_condition_is_true>
End If

'Simple if-else do one of two things based on condition 
If (<condition_to_evaluate>) Then
    <things_to_do_if_condition_is_true>
Else 
    <things_to_do_if_condition_is_false>
End If


'Chained conditionals with elseif
If (<condition1>) Then
    <things_to_do_if_condition1_is_true>
ElseIf (<condition2>)
    <things_to_do_if_condition2_is_true>
ElseIf (<condition3>)
    <things_to_do_if_condition3_is_true>
.
.
.
Else 
    <things_to_do_if_none_of_the_above_have_been_true>
End If


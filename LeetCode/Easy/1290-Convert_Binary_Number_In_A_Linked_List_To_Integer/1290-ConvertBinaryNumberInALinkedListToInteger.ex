# Definition for singly-linked list.
#
# defmodule ListNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           next: ListNode.t() | nil
#         }
#   defstruct val: 0, next: nil
# end

defmodule Solution do
  @spec get_decimal_value(head :: ListNode.t | nil) :: integer
  def get_decimal_value(head) do
    solve(head, 0)
  end

  defp solve(nil, num), do: num

  defp solve(curr, num) do
    solve(curr.next, (num * 2) + curr.val)
  end
end

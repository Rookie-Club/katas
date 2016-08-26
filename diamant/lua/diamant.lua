function diamant(lettre)

  local tableau = {}

  if lettre == "" then
    table.insert(tableau, "")
  end

  if lettre == "A" then
    table.insert(tableau, "A")
  end

  if lettre == "B" then
    table.insert(tableau, " " .. "A")
    table.insert(tableau, "B B")
    table.insert(tableau, " A")
  end

  if lettre == "C" then
    table.insert(tableau, "  A")
    table.insert(tableau, " B B")
    table.insert(tableau, "C   C")
    table.insert(tableau, " B B")
    table.insert(tableau, "  A")
  end

  return table.concat(tableau, "\n")
end

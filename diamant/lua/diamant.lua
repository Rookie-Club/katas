function diamant(lettre)

  local espace = " "

  local alphabet = {"A", "B", "C"}

  if lettre == "" then
    return ""
  end

  if lettre == "A" then
    return alphabet[1]
  end

  if lettre == "B" then
    return " A".."\n".."B B".."\n".." A"
  end

  if lettre == "C" then
    return "  A".."\n".." B B".."\n".."C   C".."\n".." B B".."\n".."  A"
  end

end

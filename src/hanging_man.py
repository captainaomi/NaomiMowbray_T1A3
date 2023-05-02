import emoji
from colored import fg, bg, attr


# Note: This does look quite repetitive, but that's on purpose!
# If I don't reset the color attribute every line, it will apply 
# that color across the ENTIRE line, and ends up looking silly. 
# By setting the color at the beginning and then using {attr("reset")} 
# at the end of every line, we get a nice even block every time!

hanging = {  
   8: f"""
      {bg(15)} ________ {attr("reset")}  
      {bg(15)} |        {attr("reset")}
      {bg(15)} |        {attr("reset")}
      {bg(15)} |        {attr("reset")}
      {bg(15)} |        {attr("reset")}
      {bg(15)} |_______ {attr("reset")}
      {bg(15)}          {attr("reset")}
      8 turns left""",

   7: f"""
      {bg(227)} ________ {attr("reset")}
      {bg(227)} |   |    {attr("reset")}
      {bg(227)} |        {attr("reset")}
      {bg(227)} |        {attr("reset")}
      {bg(227)} |        {attr("reset")}
      {bg(227)} |_______ {attr("reset")}
      {bg(227)}          {attr("reset")}
      7 turns left""",

   6: f"""
      {bg(220)} ________ {attr("reset")}
      {bg(220)} |   |    {attr("reset")}
      {bg(220)} |   o    {attr("reset")}
      {bg(220)} |        {attr("reset")}
      {bg(220)} |        {attr("reset")}
      {bg(220)} |_______ {attr("reset")}
      {bg(220)}          {attr("reset")}
      6 turns left""",

   5: f"""
      {bg(214)} ________ {attr("reset")}
      {bg(214)} |   |    {attr("reset")}
      {bg(214)} |   o    {attr("reset")}
      {bg(214)} |   |    {attr("reset")}
      {bg(214)} |        {attr("reset")}
      {bg(214)} |_______ {attr("reset")}
      {bg(214)}          {attr("reset")}
      5 turns left""",
   4: f"""
      {bg(208)} ________ {attr("reset")}
      {bg(208)} |   |    {attr("reset")}
      {bg(208)} |  \o    {attr("reset")}
      {bg(208)} |   |    {attr("reset")}
      {bg(208)} |        {attr("reset")}
      {bg(208)} |_______ {attr("reset")}
      {bg(208)}          {attr("reset")}
      4 turns left""",

   3: f"""
      {bg(196)} ________ {attr("reset")}
      {bg(196)} |   |    {attr("reset")}
      {bg(196)} |  \o/   {attr("reset")}
      {bg(196)} |   |    {attr("reset")}
      {bg(196)} |        {attr("reset")}
      {bg(196)} |_______ {attr("reset")}
      {bg(196)}          {attr("reset")}
      3 turns left""",

   2: f"""
      {bg(88)} ________ {attr("reset")}
      {bg(88)} |   |    {attr("reset")}
      {bg(88)} |  \o/   {attr("reset")}
      {bg(88)} |   |    {attr("reset")}
      {bg(88)} |  /     {attr("reset")}
      {bg(88)} |_______ {attr("reset")}
      {bg(88)}          {attr("reset")}
      2 turns left""",

   1: f"""
      {bg(52)} ________ {attr("reset")}
      {bg(52)} |   |    {attr("reset")}
      {bg(52)} |   o/   {attr("reset")}
      {bg(52)} |   |    {attr("reset")}
      {bg(52)} |  / \   {attr("reset")}
      {bg(52)} |_______ {attr("reset")}
      {bg(52)}          {attr("reset")}
      Oh gosh, you're on your last chance...""",

   0:  f"""
      {bg(0)} ________ {attr("reset")}
      {bg(0)} |   |    {attr("reset")}
      {bg(0)} |   o    {attr("reset")}
      {bg(0)} |  /|\   {attr("reset")}
      {bg(0)} |  / \   {attr("reset")}
      {bg(0)} |_______ {attr("reset")}
      {bg(0)}          {attr("reset")}
      Ba-bow, you lose (and so does our unfortunate man)."""
}

function addMath1()
{
   //テキストエリアと挿入する文字列を取得
   var area = document.getElementById('inp_bd');
   var text = "$$";
   //カーソルの位置を基準に前後を分割して、その間に文字列を挿入
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}

function addMath2()
{
   var area = document.getElementById('inp_bd');
   var text = "$$ $$";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}

function addLB()
{
   var area = document.getElementById('inp_bd');
   var text = "\r\n";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}



function addInt()
{
   var area = document.getElementById('inp_bd');
   var text = "\\int";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}

function addFrac()
{
   var area = document.getElementById('inp_bd');
   var text = "\\frac{}{}";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}

function addPar()
{
   var area = document.getElementById('inp_bd');
   var text = "\\left(\\right)";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}

function addBracket()
{
   var area = document.getElementById('inp_bd');
   var text = "\\left\\langle\\right\\rangle";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}

function addsqrt()
{
   var area = document.getElementById('inp_bd');
   var text = "\\sqrt{}";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}

function addbm()
{
   var area = document.getElementById('inp_bd');
   var text = "\\bm{}";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}

function addpd()
{
   var area = document.getElementById('inp_bd');
   var text = "\\partial";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}

function addVect()
{
   var area = document.getElementById('inp_bd');
   var text = "\\left(\\begin{array}{cc} \n {} \\\\ {} \n\\end{array} \\right)";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}

function addMtrx()
{
   var area = document.getElementById('inp_bd');
   var text = "\\left( \\begin{array}{cc} \n {} & {} \\\\ \n {} & {} \n\\end{array} \\right)";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}


function addCh()
{
   var area = document.getElementById('inp_bd');
   var text = "\\ch{}";
   area.value = area.value.substr(0, area.selectionStart)
   + text
   + area.value.substr(area.selectionStart);
}




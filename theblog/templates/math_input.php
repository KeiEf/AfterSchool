<section class="accordion">
  <div class="accordion__container">
    <h4 class="accordion__title js-accordion-title">LaTeX簡単入力</h4>
    <div class="accordion__content">


<div class="tabs">
  <input id="all" type="radio" name="tab_item" checked>
  <label class="tab_item" for="all">HTML/基本</label>
  <input id="programming" type="radio" name="tab_item">
  <label class="tab_item" for="programming">演算</label>
  <input id="design" type="radio" name="tab_item">
  <label class="tab_item" for="design">デザイン</label>

  <div class="tab_content" id="all_content">
    <div class="tab_content_description">

        <div class="container">
        <div class="row row-cols-8">

           <div class="col"><button onclick="addbr();" class="btn btn-secondary">
              <p id="inp">改行</p></button></div>

           <div class="col"><button onclick="addList();" class="btn btn-secondary">
              <p id="inp"><i class="fas fa-list"></i></p></button></div>

           <div class="col"><button onclick="addEnum();" class="btn btn-secondary">
              <p id="inp"><i class="fas fa-list-ol"></i></p></button></div>

           <div class="col"><button onclick="addMath1();" class="btn btn-secondary">
              <p id="inp">$$</p></button></div>

           <div class="col"><button onclick="addand();" class="btn btn-secondary">
              <p id="inp">&</p></button></div>

           <div class="col"><button onclick="addCurly();" class="btn btn-secondary">
              <p id="inp">{ }</p></button></div>

           <div class="col"><button onclick="addeq();" class="btn btn-secondary">
              <p id="inp">=</p></button></div>

           <div class="col"><button onclick="addSup();" class="btn btn-secondary">
              <p id="inp">$x^\Box$</p></button></div>

           <div class="col"><button onclick="addIndex();" class="btn btn-secondary">
              <p id="inp">$x_\Box$</p></button></div>

           <div class="col"><button onclick="addDelta();" class="btn btn-secondary">
              <p id="inp">$\Delta$</p></button></div>

           <div class="col"><button onclick="addnabla();" class="btn btn-secondary">
              <p id="inp">$\nabla$</p></button></div>

           <div class="col"><button onclick="addcdot();" class="btn btn-secondary">
              <p id="inp">$\cdot$</p></button></div>

           <div class="col"><button onclick="addtimes();" class="btn btn-secondary">
              <p id="inp">$\times$</p></button></div>

           <div class="col"><button onclick="addSum();" class="btn btn-secondary">
              <p id="inp">$\sum$</p></button></div>


           <div class="col"><button onclick="addInt();" class="btn btn-secondary" >
              <p id="inp">$\int$</p></button></div>

           <div class="col"><button onclick="addbm();" class="btn btn-secondary" >
              <p id="inp">$\bm{x}$</p></button></div>

           <div class="col"><button onclick="addFrac();" class="btn btn-secondary">
              <p id="inp">$\frac{a}{b}$</p></button></div>

           <div class="col"><button onclick="addPar();" class="btn btn-secondary">
              <p id="inp">$\left(...\right)$</p></button></div>

           <div class="col"><button onclick="addBracket();" class="btn btn-secondary">
              <p id="inp">$\left\langle ...\right\rangle$</p></button></div>

           <div class="col"><button onclick="addpd();" class="btn btn-secondary" >
              <p id="inp">$\partial$</p></button></div>

           <div class="col"><button onclick="addsqrt();" class="btn btn-secondary" >
              <p id="inp">$\sqrt{...}$</p></button></div>

           <div class="col"><button onclick="addVect();" class="btn btn-secondary" >
              <p id="inp">(：)</p></button></div>

           <div class="col"><button onclick="addMtrx();" class="btn btn-secondary" >
              <p id="inp">(：：)</p></button></div>

           <div class="col"><button onclick="addCh();" class="btn btn-secondary" >
              <p id="inp">$\ce{H2}$</p></button></div>
        </div>
        </div>



    </div>
  </div>



  <div class="tab_content" id="programming_content">
    <div class="tab_content_description">
      <p class="c-txtsp">プログラミングの内容がここに入ります</p>
    </div>
  </div>


  <div class="tab_content" id="design_content">
    <div class="tab_content_description">
      <p class="c-txtsp">デザインの内容がここに入ります</p>
    </div>
  </div>



</div>




 
 


    </div>
  </div><!-- accordion__container -->
</section><!-- /.accordion -->

        
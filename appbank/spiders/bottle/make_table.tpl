%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>
<table border="1">
  <tr><td>no</td><td>名前</td><td>スキル名</td><td>スキル内容</td><td>リーダースキル名</td><td>リーダースキル内容</td></tr>
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>

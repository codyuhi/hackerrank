let len = objects.length;
let total = 0;
for(let i = 0; i < len; i++) {
    if(objects[i].x * len === objects[i].y * len) {
        total++;
    }
}
return total;
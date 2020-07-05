model ("3el uda-yagi") {

real r_dist, d_dist, height, length, gauge, segments, r_coeff, d_coeff;
element center, reflector, director;

length = 0.965; // phisical length: 0.95
r_coeff = 1.04;
r_dist = -0.4;
d_coeff = 0.97;
d_dist = 0.5;
height = 3;
gauge = #10; // 2.5 mm diameter
segments = 21;

center = wire(0,-length/2, height,
              0, length/2, height,
              gauge, segments);
reflector  = wire(r_dist,-length*r_coeff/2, height,
              r_dist, length*r_coeff/2, height,
              gauge, segments);
director  = wire(d_dist,-length*d_coeff/2, height,
              d_dist, length*d_coeff/2, height,
              gauge, segments);
             
voltageFeed(center, 1.0, 0.0);

azimuthPlotForElevationAngle(2.7);
elevationPlotForAzimuthAngle(0);

// frequencySweep(144.000, 146.000, 10);
setFrequency(145.000);

averageGround();
//freespace();
} 

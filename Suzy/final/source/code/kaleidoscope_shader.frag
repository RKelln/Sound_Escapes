/*
{
  "IMPORTED": {
    "video1": {
      "PATH": "./fall_fence_dance_5.mp4"
    },
		"image1": {
			"PATH": "./fishing_boats.jpg"
		}
  },
  "pixelRatio": 1
}
*/


precision mediump float;
uniform float time;
uniform vec2 resolution;

uniform sampler2D video1;
uniform sampler2D image1;

#define pi 3.14159265359

vec2 kaleido(in vec2 uv) {
	float th = atan(uv.y, uv.x);
	float r = pow(length(uv), .9);
	float f = pi / 3.5;

	th = abs(mod(th + f/4.0, f) - f/2.0) / (1.0 + r);
	//th = sin(th * 6.283 / f);

	return vec2(cos(th), sin(th)) * r * .1;
}

vec2 kaleido2(in vec2 uv)
{
	float th = atan(uv.y, uv.x);
	float r = pow(length(uv), .3);
	float t = time * 0.02;

  float p1 = sin(2. * pi * t);
  float q = 2. * pi / ( 5. + 4. * p1);
  th = abs(mod(th, q) - 0.5 * q);
	return vec2(cos(th), sin(th)) * pow(r, 1.3 + 1.3 / (1.3 + sin(2. * pi * time / 2.0 ))) * .1;
}

vec2 transform(in vec2 at) {
	vec2 v;
	float th = .02 * time;
	v.x = at.x * cos(th) - at.y * sin(th) - .2 * sin(th);
	v.y = at.x * sin(th) + at.y * cos(th) + .2 * cos(th);
	return v;
}

vec2 transform2(vec2 at)
{
	vec2 v;
	float th = .05 * time;
	v.x = at.x * cos(th) - at.y * sin(th) - .3 * sin(th);
	v.y = at.x * sin(th) + at.y * cos(th) + .3 * cos(th);
	return v;
}

vec2 crop(in vec2 uv, in vec2 res) {
    float aspect = resolution.y / resolution.x;
    if (aspect > (res.y / res.x)) {
        // if taller
        return vec2(
            (uv.x - .5) / aspect + .5,
            uv.y
        );
    } else {
        // if wider
        return vec2(
            uv.x,
            (uv.y - .5) * aspect + .5
        );
    }
}

vec2 tile(vec2 _st, float _zoom){
    _st *= _zoom;
    return fract(_st);
}

vec4 scene(vec2 at)
{
	// float x = mod(iTime / 8.0, 3.0);
	// if (x < 1.0)
	// 	return texture(iChannel0, transform(at) * 5.0);
	// if (x < 2.0)
	// 	return texture(iChannel1, transform(at) * 2.0);
	// if (x < 3.0)
	// 	return texture(iChannel2, transform(at) * 3.0);
	//return texture(iImage0, transform(at) * 2.0);
	//return fract(texture2D(video1, transform(crop(at, resolution) + time));
	//return texture2D(image1, transform(at) * 4.0 );
	//return texture2D(image1, transform2(mod(at + 0.1, 1.)) * 4.0);
	return texture2D(image1, transform2(at) * 4.0);
}


void main()
{
	vec2 uv = gl_FragCoord.xy / resolution.xy;
	uv.x = mix(-1.0, 1.0, uv.x);
	uv.y = mix(-1.0, 1.0, uv.y);
	uv.y *= resolution.y / resolution.x;

	gl_FragColor = scene(kaleido2(uv));
}

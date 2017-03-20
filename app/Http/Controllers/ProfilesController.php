<?php

namespace App\Http\Controllers;

use Auth;
use Illuminate\Http\Request;

class ProfilesController extends Controller
{
    //
    public function update()
    {

        $profile = Auth::user()->profiles->first();

        $weixin = $profile?$profile->weixin:null;

        return view('profiles.profilesupdate',compact('weixin'));
    }


    /**
     * Update or create profile
     *
     * @return \Illuminate\Http\RedirectResponse
     */
    public function store()
    {

        Auth::user()->profiles()->updateOrCreate(
            ['user_id' => Auth::user()->id ],
            request(['weixin'])
        );

        return redirect()->route('home');

    }
}

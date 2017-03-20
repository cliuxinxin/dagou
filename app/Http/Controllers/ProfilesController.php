<?php

namespace App\Http\Controllers;

use Auth;
use Illuminate\Http\Request;

class ProfilesController extends Controller
{
    //
    public function update()
    {
        return view('profiles.profilesupdate');
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

        return back();

    }
}
